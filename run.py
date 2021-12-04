# -*- coding: UTF-8 -*-

import argparse

# Main
# ==============================================================================
if (__name__ == '__main__'):
    parser = argparse.ArgumentParser()

    help_msg = \
	"""
	The apps to be executed, separated by comma.
    \tOptions:
    \t\t- scrapper
    \t\t- source_manager
    \tExamples:
    \t\tpython run.py --apps scrapper --params http://domain1.com/article1.html,http://domain2.com/article2.html
    \t\tpython run.py --apps source_manager --params http://domain1.com/article1.html
	"""
    parser.add_argument("-a", "--apps", help=help_msg)
    parser.add_argument("-e", "--exec", help=help_msg)
    parser.add_argument("-p", "--params", help=help_msg)
    args = parser.parse_args()

    if (not args.apps):
        print(help_msg)
    else:
        args_lst = args.apps.split(',')
        params_lst = args.params.split(',')
        if (not args_lst):
            print(help_msg)
        if ("scrapper" in args_lst):
            print("running scrapper")
            print(params_lst)
        if ("source_manager" in args_lst):
            print(params_lst)
            print("runnning source_manager")
