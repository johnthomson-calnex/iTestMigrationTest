import unittest, requests, json

# How to parameterize tests for interfaces
# how to run tests from top to bottom rather than alphabetical

class UnitTest(unittest.TestCase):

    def argsToJSON(arg):
        i = iter(arg)
        d = dict(zip(i, i))
        return json.dumps(d)

    def put(api):
        requests.put("{0}{1}".format("http://100g-vm9", api), headers={'Content-Type': 'application/json'}).raise_for_status()

    @classmethod
    def setUpClass(cls) -> None:
        cls.put("/api/app/mse/ptpprofile?PtpProfile=Profile_G_8265_1")

    def test_ints(self):
        a = "SFP1G"
        self.assertEqual(a, "SFP1G")

    def test_ints2(self):
        a = "SFP1G"
        self.assertEqual(a, "SFP1G")

    def test_b(self):
        a = "SFP1G"
        self.assertEqual(a, "SFP14")

    def test_a(self):
        self.skipTest("Don't need to check 1PPS")
        a = "SFP1G"
        self.assertEqual(a, "SFP1G")

    def test_ints4(self):
        a = "SFP1G"
        self.assertEqual(a, "SFP1G")

    def test_ab(self):
        x = 17
        self.assertGreaterEqual(x,0) and self.assertLessEqual(x,10)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.put("/api/app/mse/ptpprofile?PtpProfile=Profile_G_8275_1")
    
        