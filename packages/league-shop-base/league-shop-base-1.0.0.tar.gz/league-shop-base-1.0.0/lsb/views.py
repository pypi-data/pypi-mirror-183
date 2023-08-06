
from django.shortcuts import render

from . import ddragon
from . import models
from .utils.champion_rates import get_champion_rates
from .utils.skins import get_lol_client_skins


def skins_download(request):
    '''Downloads skins from ddragon'''
    lol_client_skins = get_lol_client_skins()
    if lol_client_skins is None:
        return render(
            request,
            'shop/skins_download_failure.html',
            {'error': 'Could not parse lol-client-skins data.'},
            status=400,
        )

    patch = ddragon.get_patch()
    if patch is None:
        return render(
            request,
            'shop/skins_download_failure.html',
            {'error': 'Could not fetch patch data from ddragon.'},
            status=400,
        )
    champion_rates = get_champion_rates()
    if champion_rates is None:
        return render(
            request,
            'shop/skins_download_failure.html',
            {'error': 'Could not parse lane data.'},
            status=400,
        )
    champions = ddragon.get_champions(patch)
    if champions is None:
        return render(
            request,
            'shop/skins_download_failure.html',
            {'error': 'Could not fetch champions data from ddragon.'},
            status=400,
        )
    skin_objects = ddragon.get_skins(patch, champions, champion_rates)
    if skin_objects is None:
        return render(
            request,
            'shop/skins_download_failure.html',
            {'error': 'Could not fetch champions data from ddragon.'},
            status=400,
        )
    created_count = 0
    updated_count = 0
    for skin_object in skin_objects:
        try:
            skin_id = skin_object['id']
            lol_client_data = lol_client_skins.get(skin_id)
            mythic_skins = [
                'K/DA ALL OUT Seraphine Rising Star',
                'K/DA ALL OUT Seraphine Superstar',
                'Ashen Knight Pyke',
            ]
            if skin_object['name'] in mythic_skins:
                tier = 'MYTHIC'
            elif 'Prestige' in skin_object['name']:
                tier = 'MYTHIC'
            else:
                tier = lol_client_data['skin_rarity'] if lol_client_data is not None else 'UNKNOWN'
            release_date = None if lol_client_data is None else lol_client_data['release_date']
            value = ddragon.get_skin_value(skin_id, tier, [], release_date)
            champion_data = skin_object['champion']

            try:
                champion = models.Champion.objects.get(pk=champion_data['id'])
                champion.roles = champion_data['roles']
                champion.lanes = champion_data['lanes']
                champion.save()
            except models.Champion.DoesNotExist:
                champion = models.Champion.objects.create(**champion_data)

            skin_object['tier'] = tier
            skin_object['value'] = value
            skin_object['champion'] = champion
            obj = models.Skin.objects.get(id=skin_object['id'])
            obj.name = skin_object['name']
            obj.champion = skin_object['champion']
            obj.tier = skin_object['tier']
            obj.value = skin_object['value']
            obj.save()
            updated_count += 1
        except models.Skin.DoesNotExist:
            models.Skin.objects.create(**skin_object)
            created_count += 1
    return render(
        request,
        'shop/skins_download_success.html',
        {'message': f'{created_count}(s) skins created. {updated_count}(s) skins updated.'},
    )
