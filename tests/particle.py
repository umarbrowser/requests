from stem.control import Controller

with Controller.from_port(port = 9051) as controller:
    controller.authenticate()

    bytes_read = controller.get_info('traffic/read')
    bytes_written = controller.get_info('traffic/written')

    print('My Tor relay read %s bytes and written %s.' % (bytes_read, bytes_written))