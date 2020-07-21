"""
This is script getting block information MOC State contract
18/07/2020
"""

from moneyonchain.manager import ConnectionManager
from moneyonchain.moc import MoCState
from moneyonchain.rdoc import RDOCMoCState

import datetime

import time

def block_info(block):
    
    
    network = 'mocMainnet2'
    connection_manager = ConnectionManager(network=network)
    #print("Connecting to %s..." % network)
    #print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

    if connection_manager.options['networks'][network]['app_mode'] == 'MoC':
        moc_state = MoCState(connection_manager)
    else:
        moc_state = RDOCMoCState(connection_manager)

    n_block = int(block)

    if isinstance(block, int):
        n_block = int(connection_manager.block_number)
    if n_block <= 0:
        n_block = int(connection_manager.block_number)
   
    hours_delta = 0
   

    

    ts = connection_manager.block_timestamp(n_block)
    dt = ts - datetime.timedelta(hours=hours_delta)
    d_timestamp = dt.strftime("%Y-%m-%d %H:%M:%S")

    d_info_data = dict()

    d_info_data['blockNumber'] = n_block
    d_info_data['Timestamp'] = d_timestamp


    # bitcoin price

    d_info_data['BTCprice'] = float( moc_state.bitcoin_price(block_identifier=n_block) )


    # Moving average
    d_info_data['EMAvalue'] = float( moc_state.bitcoin_moving_average(block_identifier=n_block) )

    # days to settlement, 0 is the day of the settlement
    d_info_data['daysToSettlement'] = int(moc_state.days_to_settlement(block_identifier=n_block))

    # bkt_0 Storage DOC
    d_info_data['C0_getBucketNDoc'] = float( moc_state.bucket_ndoc(str.encode('C0'), block_identifier=n_block) )


    # bkt_0 Storage BPro
    d_info_data['C0_getBucketNBPro'] = float( moc_state.bucket_nbpro(str.encode('C0'), block_identifier=n_block) )

    # bkt_0 Storage BTC
    d_info_data['C0_getBucketNBTC'] = float( moc_state.bucket_nbtc(str.encode('C0'), block_identifier=n_block) )

    # bkt_0 Storage InrateBag
    d_info_data['C0_getInrateBag'] = float( moc_state.get_inrate_bag(str.encode('C0'), block_identifier=n_block) )

    # bkt_0 Storage Coverage
    d_info_data['C0_coverage'] = float( moc_state.coverage(str.encode('C0'), block_identifier=n_block) )

    # bkt_0 Storage Leverage
    d_info_data['C0_leverage'] = float( moc_state.leverage(str.encode('C0'), block_identifier=n_block) )

    # bkt_2 Storage DOC
    d_info_data['X2_getBucketNDoc'] = float( moc_state.bucket_ndoc(str.encode('X2'), block_identifier=n_block) )

    # bkt_2 Storage BPro
    d_info_data['X2_getBucketNBPro'] = float( moc_state.bucket_nbpro(str.encode('X2'), block_identifier=n_block) )

    # bkt_2 Storage BTC
    d_info_data['X2_getBucketNBTC'] = float( moc_state.bucket_nbtc(str.encode('X2'), block_identifier=n_block) )

    # bkt_2 Inrate Bag
    d_info_data['X2_getInrateBag'] = float( moc_state.get_inrate_bag(str.encode('X2'), block_identifier=n_block) )

    # bkt_2 Coverage
    d_info_data['X2_coverage'] = float( moc_state.coverage(str.encode('X2'), block_identifier=n_block) )

    # bkt_2 Storage Leverage
    d_info_data['X2_leverage'] = float( moc_state.leverage(str.encode('X2'), block_identifier=n_block) )

    # Global Coverage
    d_info_data['globalCoverage'] = float( moc_state.global_coverage(block_identifier=n_block) )

    # Bitpro total supply in system
    d_info_data['bproTotalSupply'] = float( moc_state.bitpro_total_supply(block_identifier=n_block) )

    # All DOC in circulation
    d_info_data['docTotalSupply'] = float( moc_state.doc_total_supply(block_identifier=n_block) )

    # RBTC in sytem
    d_info_data['rbtcInSystem'] = float( moc_state.rbtc_in_system(block_identifier=n_block) )

    # BPro Tec price
    d_info_data['bproTecPrice'] = float( moc_state.bpro_tec_price(block_identifier=n_block) )

    # BTC2X Tec price
    d_info_data['BTC2XTecPrice'] = float( moc_state.btc2x_tec_price(str.encode('X2'), block_identifier=n_block) )

    


    return d_info_data
