import unittest
from pygpet.scripts import p, sep, write


class TestP(unittest.TestCase):

    
    def test_p(self):
        p_return = p("this is a message", 'TESTING_TETING')
        self.assertEqual('[TESTING_TETING] this is a message', p_return)

        content = {
            'field_1':'value_1',
        }
        p_return = p(content, 'TESTING_TETING')
        self.assertEqual('[TESTING_TETING] {\n    "field_1": "value_1"\n}', p_return)



    def test_sep(self):
        p_return = sep(fixed_date_time="TESTING_TETING")
        self.assertEqual(f'[TESTING_TETING] {"-"*60}', p_return)




unittest.main()

