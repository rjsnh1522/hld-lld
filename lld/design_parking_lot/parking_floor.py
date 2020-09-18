from enums.parking_spot_type import ParkingSpotType
from parking_display_board import ParkingDisplayBoard


class ParkingFloor:
    def __init__(self, name):
        self.__name = name
        self.__handicapped_spots = {}
        self.__compact_spots = {}
        self.__large_spots = {}
        self.__motorcycle_spots = {}
        self.__electric_spots = {}
        self.__info_portals = {}
        self.__display_board = ParkingDisplayBoard()

    def add_parking_spot(self, spot):
        switcher = {
            ParkingSpotType.HANDICAPPED: self.__handicapped_spots.put(spot.get_number(), spot),
            ParkingSpotType.COMPACT: self.__compact_spots.put(spot.get_number(), spot),
            ParkingSpotType.LARGE: self.__large_spots.put(spot.get_number(), spot),
            ParkingSpotType.MOTORCYCLE: self.__motorcycle_spots.put(spot.get_number(), spot),
            ParkingSpotType.ELECTRIC: self.__electric_spots.put(spot.get_number(), spot),
        }
        switcher.get(spot.get_type(), "Wrong parking spot type")

    def assign_vehicle_to_Spot(self, vehicle, spot):
        spot.assign_vehicle(vehicle)
        switcher = {
            ParkingSpotType.HANDICAPPED: self.update_display_board_for_handicapped.put(spot),
            ParkingSpotType.COMPACT: self.update_display_board_for_compact.put(spot),
            ParkingSpotType.LARGE: self.update_display_board_for_large.put(spot),
            ParkingSpotType.MOTORCYCLE: self.update_display_board_for_motorcycle.put(spot),
            ParkingSpotType.ELECTRIC: self.update_display_board_for_electric.put(spot),
        }
        switcher.get(spot.get_type(), "Wrong parking spot type")

    def update_display_board_for_handicapped(self, spot):
        if self.__display_board.get_handicapped_spot().get_number() == spot.get_number():
            # find another free handicapped parking and assign to display_board
            for key in self.__handicapped_spots:
                if self.__handicapped_spots.get(key).is_free():
                    self.__display_board.set_handicapped_free_spot(
                        self.__handicapped_spots.get(key)
                    )
            self.__display_board.show_empty_spot_number()

    def update_display_board_for_compact(self, spot):
        if self.__display_board.get_compact_spot().get_number() == spot.get_number():
            # find another free handicapped parking and assign to display_board
            for key in self.__compact_spots:
                if self.__compact_spots.get(key).is_free():
                    self.__display_board.set_compact_free_spot(
                        self.__compact_spots.get(key)
                    )
            self.__display_board.show_empty_spot_number()

    def update_display_board_for_large(self, spot):
        if self.__display_board.get_larger_spot().get_number() == spot.get_number():
            # find another free handicapped parking and assign to display_board
            for key in self.__large_spots:
                if self.__large_spots.get(key).is_free():
                    self.__display_board.set_large_free_spot(
                        self.__large_spots.get(key)
                    )
            self.__display_board.show_empty_spot_number()

    def update_display_board_for_motorcycle(self, spot):
        if self.__display_board.get_motorcycle_spot().get_number() == spot.get_number():
            for key in self.__motorcycle_spots:
                if self.__motorcycle_spots.get(key).is_free():
                    self.__display_board.set_motorcycle_free_spot(
                        self.__motorcycle_spots.get(key)
                    )
            self.__display_board.show_empty_spot_number()

    def update_display_board_for_electric(self, spot):
        if self.__display_board.get_electric_spot().get_number() == spot.get_number():
            # find another free handicapped parking and assign to display_board
            for key in self.__electric_spots:
                if self.__electric_spots.get(key).is_free():
                    self.__display_board.set_electric__free_spot(
                        self.__electric_spots.get(key)
                    )
            self.__display_board.show_empty_spot_number()


    def free_spot(self, spot):
        spot.remove_vehicle()
        switcher = {
            ParkingSpotType.HANDICAPPED:(self.__free_handicapped_spot_count += 1),
            ParkingSpotType.COMPACT: (self.__free_compact_spot_count += 1),
            ParkingSpotType.LARGE: (self.__free_large_spot_count += 1),
            ParkingSpotType.MOTORBIKE: (self.__free_motorbike_spot_count += 1),
            ParkingSpotType.ELECTRIC: (self.__free_electric_spot_count += 1)
        }
        switcher.get(spot.get_type(), 'Wrong parking spot type!')
