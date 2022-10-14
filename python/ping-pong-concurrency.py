#!/usr/bin/python

# Date: 2022-10-14
#
# Description
# -----------
# Demo for multithreaded program running in synchronization.
# Spawned 2 threads, one prints `ping` and then waits for other thread to print `pong`
#
# We have used thread-safe queue implementation, so we’ll first look at an example that uses that.
# Python’s queue differs slightly from an unbuffered Golang channel because producers do not block
# when enqueueing items, even if the queue has a max size of one (the default). This makes the
# default queue more like a buffered channel of size one in Golang.
# This caveat forces us to use two separate queues so that one thread doesn’t just print over and
# over, as was the case in the scenario we talked about with a buffered channel of size one in Golang.
#
# Reference
# ---------
# https://www.josephbuiteweg.com/blog/ping-pong-concurrency/

import queue
import threading

def ping(ping_queue, pong_queue, num_times):
    for _ in range(num_times):
        print(ping_queue.get())
        pong_queue.put('pong')

def pong(ping_queue, pong_queue, num_times):
    for _ in range(num_times):
        ping_queue.put('ping')
        print(pong_queue.get())

def main():
    num_times = 5
    ping_queue = queue.Queue()
    pong_queue = queue.Queue()

    threads = [
        threading.Thread(target=ping, args=(ping_queue, pong_queue, num_times)),
        threading.Thread(target=pong, args=(ping_queue, pong_queue, num_times))
    ]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

main()

# Output
# ------
# ~/code/sample-programs patch-1$ python python/ping-pong-concurrency.py
# ping
# pong
# ping
# pong
# ping
# pong
# ping
# pong
# ping
# pong
