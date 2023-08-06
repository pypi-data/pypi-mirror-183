"""
    Copyright 2022 Stéphane De Mita

    lzmp is a simple wrapper around the multiprocessing module,
    allowing the lazy programmer to run batches of processes.

    lzmp contains the class Pool which lets the user specify one or more
    callable objects (such as functions) along with lists or argument to
    process. lzmp collects the return value of each call and return
    the whole lot as a list, keeping the original submission order. For
    a single type of callable, the standalone function run wraps the
    wrapper and allows one-line parallelization.

    lzmp is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    lzmp is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with lzmp.  If not, see <http://www.gnu.org/licenses/>.
"""

__version__ = '0.1'

import multiprocessing, random, queue

class Pool:
    """
    Class to run tasks in parallel. Can be used to run different
    functions at once.

    *max_threads* can be passed as an argument at object creation to
    limit the number of processes created simultaneously. Values below
    1 and ``None`` are ignored.
    """

    def __init__(self, max_threads=None):
        self._tasks = [] # the list of  functions to process
        self._queue = multiprocessing.Queue() # the queue used to collect return values
        self._idx = 0 # counter used to order results
        self.max_threads = max_threads

    @property
    def max_threads(self):
        """ maximum number of simultaneous processes """
        return self._max_threads

    @max_threads.setter
    def max_threads(self, max_threads):
        if max_threads is not None:
            if not isinstance(max_threads, int): raise TypeError
            if max_threads < 1: raise ValueError('max_threads must be None or positive')
        self._max_threads = max_threads

    def _wrapper(self, f, idx): # generates the function which will be actually sent to a subprocess
        def task(*args):
            self._queue.put((f(*args), idx)) # the task index is bound to its outcome
        return task

    def add(self, f, args):
        """
        Add a type of tasks.

        *f*: callable.
        *args*: iterable of arguments values (each as a list of tuples).
        """
        for arg in args:
            self._tasks.append((self._wrapper(f, self._idx), arg))
            self._idx += 1

    def _start(self):
        if len(self._waiting):
            p = self._waiting.pop(0)
            p.start()
            self._started.append(p)
            return True
        else:
            return False

    def run(self, final=None, final_args=None, shuffle=False):
        """
        Run the requested tasks. If *shuffle* is true, the order of
        tasks is randomized. Return a list of return values of the
        called function (order is not altered by shuffling). If *final*
        is not ``None``, call this function on this list and return the
        result. The callable passed as *final* will receive the combined
        return values of the callable passed to :meth:`.add` as first
        argument and, if specified, *final_args* as second argument.
        """
        if not len(self._tasks): return []
        self._waiting = [multiprocessing.Process(target=f, args=args) for (f, args) in self._tasks]
        if shuffle: random.shuffle(self._waiting)
        n = len(self._waiting)
        results = [None] * self._idx
        self._started = []
        if self._max_threads is None: nt = multiprocessing.cpu_count()
        else: nt = min(multiprocessing.cpu_count(), self._max_threads)
        for _ in range(nt):
            if not self._start():
                break
        c = 0
        err = 0
        while c < n:
            try:
                res, idx = self._queue.get(timeout=1)
                c += 1
            except queue.Empty as e:
                if not set(p.exitcode for p in self._started) <= {None, 0}:
                    for p in self._started:
                        if p.exitcode is None: p.terminate()
                    err = 1
                    break
                continue
            results[idx] = res
            self._start()
        self._idx = 0
        self._tasks = []
        if err:
            raise RuntimeError('at least one error occurred in parallelized processes: see details above')
        if final is not None:
            if final_args is not None: return final(results, final_args)
            else: return final(results)
        else: return results

def run(f, args, final=None, final_args=None, max_threads=None, shuffle=False):
    """
    Convenience function to parallelise a single type of tasks.
    Arguments are the same as for Parallel.add() and Parallel.run() (for
    *shuffle*), and it returns a list like run().
    """
    p = Pool(max_threads)
    p.add(f, args)
    return p.run(final, final_args, shuffle)

def wrap(iterable):
    """
    Return a generator wherein each item yields by *iterable* is
    included as a single-item tuple.
    """
    return ((i,) for i in iterable)
