#!/usr/bin/env python

import urllib
import time
import sys
import argparse

# Get command line input
parser = argparse.ArgumentParser(description='Monitor website responsiveness.')
parser.add_argument('url', help='URL of the site to monitor, e.g., \
    http://www.google.com/', type=str)
parser.add_argument('-a', '--alert', help='Alert threshold (in seconds).', \
    type=float, default=3)
parser.add_argument('-m', '--min', help='Minimum acceptable response time \
    (in seconds).', type=float, default=0.5)
parser.add_argument('-i', '--interval', help='Monitoring interval\
    (in seconds).', type=float, default=1)
args = parser.parse_args()

# Initialize variables
url = args.url
minimum_response_time = round(args.min, 3)
alert_threshold = round(args.alert, 3)
interval = round(args.interval, 3)

# Initialize counters
slow_responses = 0
alerts = 0
monitor_start_time = time.time()

# Print welcome
print '\nMonitoring: ' + url
print 'Minimum acceptable response time: ' + str(minimum_response_time) \
    + ' seconds'
print 'Alert threshold: ' + str(alert_threshold) + ' seconds'
print 'Interval: ' + str(interval) + ' seconds'
print 'Start time: ' + time.strftime('%a, %d %b %Y %H:%M:%S', \
    time.localtime())
print '\n' + '-' * 80 + '\n'

# Start loop
while True:
    try:
        start = time.time()
        f = urllib.urlopen(url)
        response_time = time.time() - start
        output =''
        if response_time > minimum_response_time:
            if response_time > alert_threshold:
                alerts = alerts + 1
                output = output + '[ALERT] '
            output = output + time.strftime('%a, %d %b %Y %H:%M:%S', \
                time.localtime()) + ': ' + str(round(response_time, 2)) \
                + ' seconds'
            slow_responses = slow_responses + 1
            print output;
        time.sleep(interval)
    except (KeyboardInterrupt, SystemExit):
        print '\n' + '-' * 80
        print '\nStopped at ' + time.strftime('%a, %d %b %Y %H:%M:%S', \
            time.localtime()) + '.'
        print 'Duration: ' + str(round((time.time() - monitor_start_time), 2)) + ' seconds'
        print 'Slow responses (longer than ' + str(minimum_response_time) \
            + ' seconds): ' + str(slow_responses)
        print 'Alerts (longer than ' + str(alert_threshold) + ' seconds): ' \
            + str(alerts) + '\n'
        sys.exit(0)
