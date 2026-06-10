import unittest
from BTTH import calculate_total_revenue


class TestCalculateTotalRevenue(unittest.TestCase):

    # Test Case 1
    def test_booked_and_cancelled_tickets(self):
        tickets = [
            {
                "ticket_id": "T01",
                "price": 500.0,
                "status": "Booked"
            },
            {
                "ticket_id": "T02",
                "price": 300.0,
                "status": "Cancelled"
            },
            {
                "ticket_id": "T03",
                "price": 500.0,
                "status": "Booked"
            }
        ]

        expected = 1000.0

        actual = calculate_total_revenue(tickets)

        self.assertEqual(expected, actual)

    # Test Case 2
    def test_empty_ticket_list(self):
        tickets = []

        expected = 0.0

        actual = calculate_total_revenue(tickets)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()