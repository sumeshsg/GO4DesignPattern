class EventReceiver(object):
    _monitor = []
    last_message = None

    def attach(self, monitor):
        self._monitor.append(monitor)

    def detach(self, monitor):
        self._monitor.remove(monitor)

    def notify(self):
        for monitor in self._monitor:
            monitor.update()

    def log_message(self, message):
        self.last_message = message
        self.notify()
