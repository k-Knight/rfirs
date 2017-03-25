"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryPrimaryOrganic, TileLocationChecks, IndustryLocationChecks

industry = IndustryPrimaryOrganic(id='forest',
                    prob_in_game='3',
                    prob_random='10',
                    map_colour='81',
                    prospect_chance='0.75',
                    layouts='AUTO',
                    prod_cargo_types=['WOOD'],
                    location_checks=IndustryLocationChecks(require_cluster=['forest', [20, 72, 1, 3]],
                                                           incompatible={'sawmill': 16,
                                                                         'paper_mill': 16}),
                    name='TTD_STR_INDUSTRY_NAME_FOREST',
                    extra_text_fund='string(STR_FUND_FOREST)',
                    fund_cost_multiplier='95',
                    prod_multiplier='[19]',
                    substitute='INDUSTRYTYPE_FOREST',
                    graphics_change_dates = [1935])

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_ARCTIC'].enabled = True
industry.economy_variations['BASIC_ARCTIC'].prod_cargo_types = ['WOOD', 'PULP']
industry.economy_variations['BASIC_ARCTIC'].prod_multiplier = '[18, 18]'
industry.economy_variations['MISTAH_KURTZ'].enabled = True

industry.add_tile(id='forest_tile_1',
                  foundations='return CB_RESULT_NO_FOUNDATIONS',
                  autoslope='return CB_RESULT_NO_AUTOSLOPE',
                  location_checks=TileLocationChecks(disallow_desert=True,
                                                     disallow_coast=True,
                                                     disallow_industry_adjacent=True))
industry.add_tile(id='forest_tile_2',
                  location_checks=TileLocationChecks(disallow_desert=True,
                                                     disallow_coast=True,
                                                     disallow_industry_adjacent=True))

sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDTILE_MUD_TRACKS'
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'forest_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'forest_equipment_1',
    sprites = [(10, 10, 64, 78, -31, -45)],
)
spriteset_2 = industry.add_spriteset(
    id = 'forest_equipment_2',
    sprites = [(80, 10, 64, 78, -31, -45)],
)
spriteset_3 = industry.add_spriteset(
    id = 'forest_wood_stack',
    sprites = [(150, 10, 64, 78, -31, -45)],
)

industry.add_spritelayout(
    id = 'forest_equipment_spritelayout',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1, spriteset_2],
)
industry.add_spritelayout(
    id = 'forest_wood_stack_spritelayout',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_3],
)
industry.add_magic_spritelayout(
    type = 'slope_aware_trees',
    base_id = 'forest_slope_aware_ground_with_trees_uniform',
    config = {'ground_sprite': 3943,
              'trees_default': [1712, 1712, 1712, 1712, 1712, 1712, 1712, 1712, 1712],
              'trees_snow': [1768, 1768, 1768, 1768, 1768, 1768, 1768, 1768, 1768],
              'trees_tropic': [1838, 1838, 1838, 1838, 1838, 1838, 1838, 1838, 1838]}
)
industry.add_magic_spritelayout(
    type = 'slope_aware_trees',
    base_id = 'forest_slope_aware_ground_with_trees_dying',
    config = {'ground_sprite': 3943,
              'trees_default': [1710, 1715, 1595, 1714],
              'trees_snow': [1766, 1771, 1767, 1770],
              'trees_tropic': [1873, 1870, 1839, 1836]}
)


industry.add_industry_layout(
    id = 'forest_layout_1',
    layout = [(0, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (0, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (0, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (1, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (1, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (1, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_dying'),
              (2, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (2, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (2, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_dying'),
              (3, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_dying'),
              (3, 1, 'forest_tile_2', 'forest_wood_stack_spritelayout'),
              (3, 2, 'forest_tile_2', 'forest_equipment_spritelayout')
    ]
)
industry.add_industry_layout(
    id = 'forest_layout_2',
    layout = [(0, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (0, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (0, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (0, 3, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (0, 4, 'forest_tile_2', 'forest_equipment_spritelayout'),
              (1, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (1, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (1, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (1, 3, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_dying'),
              (1, 4, 'forest_tile_2', 'forest_wood_stack_spritelayout'),
              (2, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (2, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (2, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (2, 3, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_dying'),
              (2, 4, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_dying')
    ]
)
industry.add_industry_layout(
    id = 'forest_layout_3',
    layout = [(0, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (0, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (0, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (0, 3, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (1, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (1, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (1, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (1, 3, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (2, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (2, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_dying'),
              (2, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_dying'),
              (2, 3, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_dying'),
              (3, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_dying'),
              (3, 1, 'forest_tile_2', 'forest_wood_stack_spritelayout'),
              (3, 2, 'forest_tile_2', 'forest_equipment_spritelayout'),
              (3, 3, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_dying')
    ]
)
industry.add_industry_layout(
    id = 'forest_layout_4',
    layout = [(0, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (0, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (0, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (0, 3, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (1, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (1, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (1, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (1, 3, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_dying'),
              (2, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (2, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (2, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_dying'),
              (2, 3, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_dying'),
              (3, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (3, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_dying'),
              (3, 2, 'forest_tile_2', 'forest_equipment_spritelayout'),
              (4, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (4, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (4, 2, 'forest_tile_2', 'forest_wood_stack_spritelayout'),
              (5, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (5, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
              (5, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_dying')
    ]
)
