from collections import defaultdict

coin_dict = defaultdict(lambda: {'basis': 0, 'amount': 0, 'tax': 0, 'basisbasis': 0})
coin_dict['ETH'] = {'basis': -29702.5151, 'amount': 0.011, 'tax': 0}
coin_dict['XMR'] = {'basis': -2355, 'amount': 0.022, 'tax': 0}