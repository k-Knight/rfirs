from cargo import Cargo

cargo = Cargo(id = 'fertiliser',
              type_name = 'string(STR_CARGO_NAME_FERTILISER)',
              unit_name = 'string(STR_CARGO_NAME_FERTILISER)',
              type_abbreviation = 'string(STR_CID_FERTILISER)',
              sprite = 'NEW_CARGO_SPRITE',
              weight = '0.5625',
              station_list_colour = '75',
              cargo_payment_list_colour = '75',
              is_freight = '1',
              cargo_classes = 'bitmask(CC_PIECE_GOODS, CC_BULK, CC_COVERED)',
              cargo_label = 'FERT',
              town_growth_effect = 'TOWNGROWTH_NONE',
              town_growth_multiplier = '1.0',
              units_of_cargo = '84',
              items_of_cargo = 'string(STR_CARGO_UNIT_FERTILISER)',
              penalty_lowerbound = '6',
              single_penalty_length = '36',
              price_factor = '128.11088562',
              capacity_multiplier = '1',
              icon_indices = (8, 1))

