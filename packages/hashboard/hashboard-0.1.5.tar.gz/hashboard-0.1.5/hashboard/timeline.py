import numpy as np
import pandas as pd

from .parsing import to_unix_time

class Timeline(object):

    def __init__(self, unix_times, current_price, price, block_reward, hashes_per_block):

        self.unix_times = unix_times
        self.pd_index = pd.to_datetime(unix_times, unit='s')
        self.current_price = current_price

        btc_per_th_day = 8.64e16 * block_reward / hashes_per_block

        # minimal sufficient statistics for mining profitability:
        self.rollouts = {'usd_per_btc': price, 'btc_per_th_day': btc_per_th_day}

    def evaluate_miner(self,
                        miner_usd_cost,
                        terahashes,
                        daily_usd_cost,
                        start_time,
                        lifespan=4,
                        contract=1):

        start_time = to_unix_time(start_time)
        end_time = int(start_time + lifespan * 31556952)
        contract_end_time = int(start_time + contract * 31556952)

        ut = self.unix_times.reshape((-1, 1))

        # compute statistics unaware of uptime:
        daily_btc_gross = terahashes * self.rollouts['btc_per_th_day']
        daily_usd_gross = daily_btc_gross * self.rollouts['usd_per_btc']
        daily_usd_net = daily_usd_gross - daily_usd_cost
        daily_btc_net = daily_usd_net / self.rollouts['usd_per_btc']

        # the period of time for which the miner is online:
        can_be_online = (ut >= start_time) & (ut <= end_time)
        is_profitable = daily_usd_gross > daily_usd_cost
        is_contracted = (ut <= contract_end_time)
        active_mask = can_be_online & (is_profitable | is_contracted)

        # incorporate uptime:
        daily_btc_gross *= active_mask
        daily_usd_gross *= active_mask
        daily_usd_net *= active_mask
        daily_btc_net *= active_mask

        miner_btc_cost = miner_usd_cost / self.current_price

        return {'daily_btc_gross': daily_btc_gross,
                'daily_btc_net': daily_btc_net,
                'miner_btc_cost': miner_btc_cost,
                'daily_usd_gross': daily_usd_gross,
                'daily_usd_net': daily_usd_net,
                'miner_usd_cost': miner_usd_cost}
