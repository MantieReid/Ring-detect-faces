from ring_doorbell import Ring
import os
import config









myring = Ring(config.username,config.password)

print("is my ring connected?", myring.is_connected)

# Get All devices
print("list all devices", myring.devices)
print("list all stickup cams",myring.stickup_cams)
print("list all chimes", myring.chimes)
print("list all doorbells", myring.doorbells)

for dev in list(myring.stickup_cams + myring.chimes + myring.doorbells):

    dev.update()

    print('Account ID : %s' % dev.account_id)
    print('Address :    %s' % dev.address)
    print('Family:     %s' % dev.family)
    print('ID:         %s' % dev.id)
    print('Name:       %s' % dev.name)
    print('Timezone:   %s' % dev.timezone)
    print('Wifi Name:  %s' % dev.wifi_name)
    print('Wifi RSSI:  %s' % dev.wifi_signal_strength)

    # setting dev volume
    print('Volume:     %s' % dev.volume)
    dev.volume = 11
    print('Volume:     %s' % dev.volume)

    for doorbell in myring.doorbells:

      # listing the last 15 events of any kind
      for event in doorbell.history(limit=10000):
        print('ID:       %s' % event['id'])
        print('Kind:     %s' % event['kind'])
        print('Answered: %s' % event['answered'])
        print('When:     %s' % event['created_at'])
        print('--' * 50)

      # get a event list only the triggered by motion
      events = doorbell.history(kind='motion')


    if dev.family == 'chimes':
      dev.test_sound(kind = 'ding')
      dev.test_sound(kind ='motion')


path_for_logs = os.path.join('videos_from_ring', 'videos')
if not os.path.exists(path_for_logs):  # if folder for the logs does exist, then create it.
  os.makedirs(path_for_logs)

doorbell = myring.doorbells[0]

eventidlist = [6733320337061648197, 6733320654889228101, 6733321161695369029, 6733353472734336837, 6733325576921749317, 6733353472734336837,6733361474258409285]

for x in eventidlist:
  doorbell.recording_download(recording_id=x,filename= str(x) + 'test23.mp4',override=False)

