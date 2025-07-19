# test_zerotrustnetworksentinel.py
"""
Tests for ZeroTrustNetworkSentinel module.
"""

import unittest
from zerotrustnetworksentinel import ZeroTrustNetworkSentinel

class TestZeroTrustNetworkSentinel(unittest.TestCase):
    """Test cases for ZeroTrustNetworkSentinel class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ZeroTrustNetworkSentinel()
        self.assertIsInstance(instance, ZeroTrustNetworkSentinel)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ZeroTrustNetworkSentinel()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
