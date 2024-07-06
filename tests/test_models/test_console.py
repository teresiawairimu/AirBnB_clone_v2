import unittest
from console import HBNBCommand
from models import storage
from models.state import State
from models.place import Place


class TestHBNBCommand(unittest.TestCase):
    """Tests for HBNBCommand."""

    def setUp(self):
        """Set up test environment."""
        self.cli = HBNBCommand()

    def tearDown(self):
        """Clean up after each test."""
        storage.close()
        storage.reload()

    def test_create_with_parameters(self):
        """Test create command with parameters."""
        initial_count = len(storage.all(State))
        self.cli.onecmd('create State name="California"')
        self.assertEqual(len(storage.all(State)), initial_count + 1)
        state = list(storage.all(State).values())[0]
        self.assertEqual(state.name, "California")

    def test_create_place_with_parameters(self):
        """Test create command for Place with multiple parameters."""
        initial_count = len(storage.all(Place))
        self.cli.onecmd('
                        create Place city_id="0001"
                        user_id="0001"
                        name="My_little_house"
                        number_rooms=4
                        number_bathrooms=2
                        max_guest=10
                        price_by_night=300
                        latitude=37.773972
                        longitude=-122.431297')
        self.assertEqual(len(storage.all(Place)), initial_count + 1)
        place = list(storage.all(Place).values())[0]
        self.assertEqual(place.city_id, "0001")
        self.assertEqual(place.user_id, "0001")
        self.assertEqual(place.name, "My little house")
        self.assertEqual(place.number_rooms, 4)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 10)
        self.assertEqual(place.price_by_night, 300)
        self.assertAlmostEqual(place.latitude, 37.773972)
        self.assertAlmostEqual(place.longitude, -122.431297)


if __name__ == '__main__':
    unittest.main()
