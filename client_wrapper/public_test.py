import banjo_driver
import contextlib
import http_response
import http_server
import logging
import time

logger = logging.getLogger(__name__)

def _run_test_iterations(driver, iterations, output_dir):
    """Use the given client driver to run the specified number of iterations.

    Given an NDT client driver, run NDT tests for the given number of
    iterations. On completion of each test, save the result to disk and print
    the result to the console.

    Args:
        driver: An NDT client driver that supports the perform_test API.
        iterations: The total number of test iterations to run.
        output_dir: Directory in which to result file.
    """
    for i in range(iterations):
        print 'starting iteration %d...' % (i + 1)
        result = driver.perform_test()

        print result



def main():
    with open('/Users/LavalleF/Documents/mlab/ndt-e2e-ansible/http_replays/onebox-replay.firefox45-noclick.yaml') as replay_file:
#    with open('/Users/LavalleF/Documents/mlab/ndt-e2e-ansible/http_replays/replay-banjo-2016-06-07.yaml') as replay_file:
        replays = http_response.parse_yaml(replay_file.read())
        print "these are the replays "
        print replays
    with contextlib.closing(http_server.create_replay_server_manager(
            replays, 'ndt.iupui.mlab1.iad04.measurement-lab.org')) as replay_server_manager:
        replay_server_manager.start()

        url = 'http://localhost:%d/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8' % replay_server_manager.port

        print url

        driver = banjo_driver.BanjoDriver('chrome', url)
        time.sleep(60)
        #_run_test_iterations(driver, 2, '/Users/LavalleF/Desktop/')

if __name__ == '__main__':
    main()