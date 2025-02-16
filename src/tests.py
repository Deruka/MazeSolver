import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )


    def test_maze_create_small(self):
        num_cols = 2
        num_rows = 2
        m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m2._cells),
            num_cols,
        )
        self.assertEqual(
            len(m2._cells[0]),
            num_rows,
        )

    def test_maze_create_rectangular(self):
        num_cols = 5
        num_rows = 10
        m3 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m3._cells),
            num_cols,
        )
        self.assertEqual(
            len(m3._cells[0]),
            num_rows,
        )

    def test_maze_cells_have_walls(self):
        # Create a small maze to test
        m4 = Maze(0, 0, 3, 3, 10, 10)
        
        # Check walls of the top-left cell (position 0,0)
        cell = m4._cells[0][0]
        self.assertTrue(cell.has_left_wall)
        self.assertTrue(cell.has_right_wall)
        self.assertTrue(cell.has_top_wall)
        self.assertTrue(cell.has_bottom_wall)

    def test_maze_invalid_dimensions(self):
        # Test with negative dimensions
        with self.assertRaises(ValueError):
            Maze(0, 0, -1, 5, 10, 10)

    def test_maze_invalid_positions(self):
        # Test with negative x1, y1 coordinates
        with self.assertRaises(ValueError):
            Maze(-10, -10, 5, 5, 10, 10)

    def test_cell_center_calculation(self):
        # Create a maze with 10x10 cells
        m = Maze(0, 0, 1, 1, 10, 10)
        center = m._cells[0][0].get_center_point()
        # For a cell at (0,0) with size 10x10, center should be at (5,5)
        self.assertEqual(center.x, 5)
        self.assertEqual(center.y, 5)

    def test_maze_cell_access(self):
        num_cols = 3
        num_rows = 4
        m = Maze(0, 0, num_rows, num_cols, 10, 10)
        # Try to access each cell
        for i in range(num_cols):
            for j in range(num_rows):
                # This should not raise an error
                cell = m._cells[i][j]
                self.assertIsNotNone(cell)

    def test_cell_neighbors(self):
        m = Maze(0, 0, 2, 2, 10, 10)
        # Top-left cell (0,0)
        cell = m._cells[0][0]
        # Should have right and bottom neighbors
        self.assertIsNotNone(m._cells[1][0])  # right neighbor exists
        self.assertIsNotNone(m._cells[0][1])  # bottom neighbor exists
        # Should not have left or top neighbors (edge of maze)
        self.assertTrue(cell.has_left_wall)    # left wall should exist
        self.assertTrue(cell.has_top_wall)     # top wall should exist

    def test_break_entrance_and_exit(self):
        m = Maze(0, 0, 5, 5, 10, 10)
        # Entrance and Exit cell
        cell_ent = m._cells[0][0]
        cell_ex = m._cells[4][4]
        # Call function to break the entrance and exit
        m._break_entrance_and_exit()

        # Should have open walls Top and Bottom
        self.assertFalse(cell_ent.has_top_wall)
        self.assertFalse(cell_ex.has_bottom_wall)

    def test_reset_visited_after_breaking_walls(self):
        m = Maze(0, 0, 5, 5, 10, 10)
        m._break_entrance_and_exit()
        m._break_walls_r(0, 0)
        # Verify that visited is set to True for the specific test case cell
        for list in m._cells:
            for cell in list:
                self.assertTrue(cell.visited)
        # Reset visited
        m._reset_cells_visited()
        # Verify that visited is set to False for the specific test case cell
        for list in m._cells:
            for cell in list:
                self.assertFalse(cell.visited)

if __name__ == "__main__":
    unittest.main()
