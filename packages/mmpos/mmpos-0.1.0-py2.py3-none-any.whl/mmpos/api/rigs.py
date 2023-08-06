import mmpos.api.utils as utils
import threading
import mmpos.api.farms as farms

rig_name_table = {}

def get(farm_id):
  list = []
  if (farm_id == 'all'):
    for farm in farms.farms():
        list.append(rigs(farm['id']))
    return utils.flatten(list)
  else:
    list = rigs(farm_id)

  return list

def show(rig_id):
  pass

def all_rigs():
    all_rigs = []
    for farm in farms.farms():
        all_rigs.append(rigs(farm['id']))
    return utils.flatten(all_rigs)

def rig_name_list(refresh=False):
  if (len(rig_name_table) < 1 or refresh):
    for rig in all_rigs():
        rig_name_table[rig['id']] = rig['name']

  return rig_name_table  

def rigs(farm_id):
    rigs = utils.call_api(f'{farm_id}/rigs')
    list = []
    for rig in rigs:
        list.append(rig)
    return list

def set_rig_control(action, farm_id, rig_id, simulate=False, block=None):
    if (not simulate):
      utils.call_api(f'{farm_id}/rigs/{rig_id}/control', {}, {"control": action}, method='POST')
    else:
      action = f'simulated-{action}'
    if block:
      rig_name = rig_name_list()[rig_id]
      block(rig_name, f'{action}')
    return True

def rig_control(action, rig_id, farm_id, simulate=False, block=None):
    if (rig_id == 'all'):
        threads = []
        for rig in rigs(farm_id):
            x = threading.Thread(target=set_rig_control, args=(action.lower(), farm_id, rig['id']), 
              kwargs={'simulate': simulate, 'block': block})
            if (utils.current_thread_count(threads) > utils.MAX_THREAD_COUNT):
                threads.pop(0).join() # wait for the first thread to finish

            x.start()
            threads.append(x) 
    else:        
        set_rig_control(action.lower(), farm_id, rig_id, simulate=simulate, block=block)

    return

