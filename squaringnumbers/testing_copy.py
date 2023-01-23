def test_func():
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    # Do Not Change the code above 👆
    
    # Write your 1 line code below 👇
    squared_numbers = [num * num for num in numbers]
    # Write your code above 👆
    
    print(squared_numbers)
    
    
    with open('testing_copy.py', 'w') as file:
      file.write('def test_func():\n')
      with open('main.py', 'r') as original:
        f2 = original.readlines()[0:40]
        for x in f2:
          file.write("    " + x)
    
    with open('testing_copy_2.py', 'w') as file:
      file.write('numbers = [9, 0, 32, 8, 2, 8, 64, 29, 42, 99]\n\n')
      file.write('def test_func():\n')
      with open('main.py', 'r') as original:
        f2 = original.readlines()[2:40]
        for x in f2:
          file.write("    " + x)
    
    import testing_copy
    import testing_copy_2
    
    import unittest
    from unittest.mock import patch
    from io import StringIO
    import os
    
    class MyTest(unittest.TestCase):
      def test_1(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
          testing_copy.test_func()
          expected_print = "[1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]\n"
          self.assertEqual(fake_out.getvalue(), expected_print)
    
