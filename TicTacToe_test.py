import unittest
from TicTacToe import board

class TicTacToeWin(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TicTacToeWin, self).__init__(*args, **kwargs)
        self.TicBoard = board()

    def test_Row1Win(self):
        self.TicBoard.replace(1, 1, 'X')
        self.TicBoard.replace(1, 2, 'X')
        self.TicBoard.replace(1, 3, 'X')
        self.assertTrue(self.TicBoard.check('X')[0])
        self.assertEqual('Won on Row 1' ,self.TicBoard.check('X')[1])

    def test_Row2Win(self):
        self.TicBoard.replace(2, 1, 'X')
        self.TicBoard.replace(2, 2, 'X')
        self.TicBoard.replace(2, 3, 'X')
        self.assertTrue(self.TicBoard.check('X')[0])
        self.assertEqual('Won on Row 2' ,self.TicBoard.check('X')[1])

    def test_Row3Win(self):
        self.TicBoard.replace(3, 1, 'X')
        self.TicBoard.replace(3, 2, 'X')
        self.TicBoard.replace(3, 3, 'X')
        self.assertTrue(self.TicBoard.check('X')[0])
        self.assertEqual('Won on Row 3' ,self.TicBoard.check('X')[1])

    def test_Col1Win(self):
        self.TicBoard.replace(1, 1, 'X')
        self.TicBoard.replace(2, 1, 'X')
        self.TicBoard.replace(3, 1, 'X')
        self.assertTrue(self.TicBoard.check('X')[0])
        self.assertEqual('Won on Column 1' ,self.TicBoard.check('X')[1])

    def test_Col2Win(self):
        self.TicBoard.replace(1, 2, 'X')
        self.TicBoard.replace(2, 2, 'X')
        self.TicBoard.replace(3, 2, 'X')
        self.assertTrue(self.TicBoard.check('X')[0])
        self.assertEqual('Won on Column 2' ,self.TicBoard.check('X')[1])

    def test_Col3Win(self):
        self.TicBoard.replace(1, 3, 'X')
        self.TicBoard.replace(2, 3, 'X')
        self.TicBoard.replace(3, 3, 'X')
        self.assertTrue(self.TicBoard.check('X')[0])
        self.assertEqual('Won on Column 3' ,self.TicBoard.check('X')[1])

    def test_Diag1Win(self):
        self.TicBoard.replace(1, 1, 'X')
        self.TicBoard.replace(2, 2, 'X')
        self.TicBoard.replace(3, 3, 'X')
        self.assertTrue(self.TicBoard.check('X')[0])
        self.assertEqual('Won on Diagonal 1' ,self.TicBoard.check('X')[1])

    def test_Diag2Win(self):
        self.TicBoard.replace(1, 3, 'X')
        self.TicBoard.replace(2, 2, 'X')
        self.TicBoard.replace(3, 1, 'X')
        self.assertTrue(self.TicBoard.check('X')[0])
        self.assertEqual('Won on Diagonal 2' ,self.TicBoard.check('X')[1])


class TicTacToeFalseCheck(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TicTacToeFalseCheck, self).__init__(*args, **kwargs)
        self.TicBoard = board()

    def test_Row1Loss(self):
        self.TicBoard.replace(1, 1, 'X')
        self.TicBoard.replace(1, 2, 'O')
        self.TicBoard.replace(1, 3, 'X')
        self.assertFalse(self.TicBoard.check('X')[0])

    def test_Row2Loss(self):
        self.TicBoard.replace(2, 1, 'X')
        self.TicBoard.replace(2, 2, 'X')
        self.TicBoard.replace(2, 3, '0')
        self.assertFalse(self.TicBoard.check('X')[0])

    def test_Row3Loss(self):
        self.TicBoard.replace(3, 1, 'O')
        self.TicBoard.replace(3, 2, 'X')
        self.TicBoard.replace(3, 3, 'O')
        self.assertFalse(self.TicBoard.check('X')[0])

    def test_Col1Loss(self):
        self.TicBoard.replace(1, 1, 'O')
        self.TicBoard.replace(1, 1, 'X')
        self.TicBoard.replace(3, 1, 'X')
        self.assertFalse(self.TicBoard.check('X')[0])

    def test_Col2Loss(self):
        self.TicBoard.replace(1, 2, 'X')
        self.TicBoard.replace(2, 2, 'X')
        self.TicBoard.replace(3, 2, 'O')
        self.assertFalse(self.TicBoard.check('X')[0])

    def test_Col3Loss(self):
        self.TicBoard.replace(1, 3, 'X')
        self.TicBoard.replace(1, 3, 'O')
        self.TicBoard.replace(3, 3, 'X')
        self.assertFalse(self.TicBoard.check('X')[0])

    def test_Diag1Loss(self):
        self.TicBoard.replace(1, 1, 'X')
        self.TicBoard.replace(2, 2, 'O')
        self.TicBoard.replace(3, 3, 'X')
        self.assertFalse(self.TicBoard.check('X')[0])

    def test_Diag2Loss(self):
        self.TicBoard.replace(1, 3, 'X')
        self.TicBoard.replace(1, 3, 'X')
        self.TicBoard.replace(2, 2, 'O')
        self.assertFalse(self.TicBoard.check('X')[0])


class PotentialWin(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(PotentialWin, self).__init__(*args, **kwargs)
        self.TicBoard = board()

    def test_Row1Loss(self):
        self.TicBoard.replace(1, 1, 'X')
        self.TicBoard.replace(1, 2, 'O')
        self.TicBoard.replace(1, 3, 'X')
        self.assertFalse(self.TicBoard.check('X')[0])
if __name__ == '__main__':
    unittest.main()