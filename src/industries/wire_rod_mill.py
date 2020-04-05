from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(id='wire_rod_mill',
                             accept_cargos_with_input_ratios=[('STCB', 4), ('ACID', 2), ('SOAP', 2)],
                             combined_cargos_boost_prod=True,
                             prod_cargo_types_with_output_ratios=[('STWR', 4), ('RBAR', 3), ('ENSP', 1)],
                             prob_in_game='3',
                             prob_map_gen='5',
                             map_colour='43',
                             name='string(STR_IND_WIRE_ROD_MILL)',
                             nearby_station_name='string(STR_STATION_HEAVY_INDUSTRY_2)',
                             fund_cost_multiplier='120',
                             intro_year=1832)


industry.economy_variations['STEELTOWN'].enabled = True

industry.add_tile(id='wire_rod_mill_tile_1',
                  animation_length=71,
                  animation_looping=True,
                  animation_speed=2,
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))


spriteset_ground = industry.add_spriteset(
    type='concrete',
)
spriteset_ground_overlay = industry.add_spriteset(
    type='empty'
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 60, 64, 70, -31, -35)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 60, 64, 70, -31, -35)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 60, 64, 51, -31, -20)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 60, 64, 51, -31, -23)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 60, 64, 51, -31, -20)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 60, 64, 31, -31, 0)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 60, 64, 31, -31, 0)],
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type='white_smoke_small',
    xoffset=-5,
    yoffset=0,
    zoffset=26,
)

industry.add_spritelayout(
    id='wire_rod_mill_spritelayout_1',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='wire_rod_mill_spritelayout_2',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='wire_rod_mill_spritelayout_3',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='wire_rod_mill_spritelayout_4',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    smoke_sprites=[sprite_smoke],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='wire_rod_mill_spritelayout_5',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='wire_rod_mill_spritelayout_6',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='wire_rod_mill_spritelayout_7',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
    fences=['nw', 'ne', 'se', 'sw']
)

industry.add_industry_layout(
    id='wire_rod_mill_industry_layout_1',
    layout=[(0, 0, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_3'),
            (0, 1, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_3'),
            (0, 2, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_4'),
            (0, 3, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_6'),
            (0, 4, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_5'),
            (1, 0, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_3'),
            (1, 1, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_3'),
            (1, 2, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_7'),
            (1, 3, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_6'),
            (1, 4, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_5'),
            (2, 0, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_3'),
            (2, 1, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_1'),
            (2, 2, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_2'),
            (2, 3, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_7'),
            (2, 4, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_6'),
            ]
)
industry.add_industry_layout(
    id='wire_rod_mill_industry_layout_2',
    layout=[(0, 2, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_3'),
            (0, 3, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_3'),
            (1, 0, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_1'),
            (1, 1, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_2'),
            (1, 2, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_3'),
            (1, 3, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_3'),
            (2, 0, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_7'),
            (2, 1, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_7'),
            (2, 2, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_6'),
            (2, 3, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_6'),
            (3, 0, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_4'),
            (3, 1, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_5'),
            (3, 2, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_5'),
            (3, 3, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_5'),
            ]
)
industry.add_industry_layout(
    id='wire_rod_mill_industry_layout_3',
    layout=[(0, 0, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_3'),
            (0, 1, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_3'),
            (0, 2, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_3'),
            (0, 3, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_5'),
            (1, 0, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_3'),
            (1, 1, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_3'),
            (1, 2, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_3'),
            (1, 3, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_6'),
            (2, 0, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_5'),
            (2, 1, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_1'),
            (2, 2, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_2'),
            (2, 3, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_7'),
            (3, 0, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_5'),
            (3, 1, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_4'),
            (3, 2, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_7'),
            (3, 3, 'wire_rod_mill_tile_1', 'wire_rod_mill_spritelayout_6'),
            ]
)