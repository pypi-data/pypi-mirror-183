from __future__ import annotations
from typing import List, TypeVar, Callable, Union, overload, Optional, Any
from .predicate_class import Predicate

T = TypeVar("T")
Acc = TypeVar('Acc')


class ArrayHelper(list):
    def __init__(self, arr: List[T] = ()):
        super().__init__(arr)
    
    @staticmethod
    def __setup_predicate(predicate: Union[Predicate, Callable]) -> Predicate:
        if isinstance(predicate, Predicate):
            return predicate
        return Predicate(predicate)
    
    @overload
    def find(self, predicate: Callable[[T, Optional[int], Optional[List[T]]], bool]) -> T | None:
        ...
    
    @overload
    def find(self, predicate: Predicate) -> T | None:
        ...
    
    def find(self, predicate: Union[Predicate, Callable[[T, Optional[int], Optional[List[T]]], bool]]) -> T | None:
        """The `find()` method returns the first element in the provided array that satisfies the provided predicate.
        If no values satisfy the predicate, None is returned.
        
        - If you need the index of the found element in the array, use `findIndex()`
        - If you need to find the index of a value, use `index_of()`. (It's similar to `find_index()`, but checks each
          element for equality with the value instead of using a predicate.)
        - If you need to find if a value exists in an array, use `includes()`. Again, it checks each element for
          equality with the value instead of using a predicate.
        - If you need to find if any element satisfies the provided testing function, use `some()`
        
        :param predicate: A function to execute for each element in the array. It should return a truthy value to
                          indicate a matching element has been found.
                          The function is called with the following arguments:
                          `element`: The current element being processed in the array.
                          `index`: The index of the current element being processed in the array.
                          `array`: The array the method was called upon.
        :type predicate: Union[Predicate, Callable[[T, Optional[int], Optional[List[T]]], bool]]
        :returns: the first element in the provided array that satisfies the predicate. Otherwise, None is returned.
        :rtype: T | None
        """
        
        predicate = ArrayHelper.__setup_predicate(predicate)
        i = self.find_index(predicate)
        return None if i == -1 else self[i]
    
    @overload
    def find_index(self, predicate: Callable[[T, Optional[int], Optional[List[T]]], bool]) -> int | None:
        ...
    
    @overload
    def find_index(self, predicate: Predicate) -> int | None:
        ...
    
    def find_index(self,
                   predicate: Union[Predicate, Callable[[T, Optional[int], Optional[List[T]]], bool]]) -> int | None:
        """The find_index() method returns the index of the first element in an array that satisfies the provided
        predicate. If no elements satisfy the predicate, -1 is returned.
        
        See also the `find()` method, which returns the first element that satisfies the predicate (rather than its
        index)
        
        :param predicate: A function to execute for each element in the array. It should return a truthy value to
                          indicate a matching element has been found.
                          The function is called with the following arguments:
                          `element`: The current element being processed in the array.
                          `index`: The index of the current element being processed in the array.
                          `array`: The array the method was called upon.
        :type predicate: Union[Predicate, Callable[[T, Optional[int], Optional[List[T]]], bool]]
        :returns: the index of the first element in the array that passes the test. Otherwise, -1.
        :rtype: T | None
        """
        
        predicate = ArrayHelper.__setup_predicate(predicate)
        for i, v in enumerate(self):
            if predicate.call(v, i, self):
                return i
        return -1
    
    @overload
    def find_last(self, predicate: Callable[[T, Optional[int], Optional[List[T]]], bool]) -> T | None:
        ...
    
    @overload
    def find_last(self, predicate: Predicate) -> T | None:
        ...
    
    def find_last(self, predicate: Union[Predicate, Callable[[T, Optional[int], Optional[List[T]]], bool]]) -> T:
        """The find_last() method iterates the array in reverse order and returns the value of the first element that
        satisfies the provided predicate. If no elements satisfy the testing function, None is returned.
        
        If you need to find:
        - the *first* element that matches, use `find()`
        - the *index* of the last matching element in the array, use `find_last_index()`
        - the *index of a value*, use `index_of()`. (It's similar to `find_index()` but checks each element for equality
          with the value instead of using a predicate)
        - whether a value *exists* in an array, use `includes()`. Again, it checks each element for equality with the
          value instead of using a predicate.
        - if any element satisfies the provided testing function, use `some()`
        
        :param predicate: A function to execute for each element in the array. It should return a truthy value to
                          indicate a matching element has been found.
                          The function is called with the following arguments:
                          `element`: The current element being processed in the array.
                          `index`: The index of the current element being processed in the array.
                          `array`: The array the method was called upon.
        :type predicate: Union[Predicate, Callable[[T, Optional[int], Optional[List[T]]], bool]]
        :returns: the value of the element in the array with the highest index value that satisfies the provided
                  predicate; None if no matching element is found.
        :rtype: T | None
        """
        
        predicate = ArrayHelper.__setup_predicate(predicate)
        i = self.find_last_index(predicate)
        return None if i == -1 else self[i]
    
    @overload
    def find_last_index(self, predicate: Callable[[T, Optional[int], Optional[List[T]]], bool]) -> int | None:
        ...
    
    @overload
    def find_last_index(self, predicate: Predicate) -> int | None:
        ...
    
    def find_last_index(self,
                        predicate: Union[
                            Predicate, Callable[[T, Optional[int], Optional[List[T]]], bool]]) -> int | None:
        """The `find_last_index()` method iterates the array in reverse order and returns the index of the first element
        that satisfies the provided predicate. If no elements satisfy the testing function, -1 is returned.
        
        See also the `find_last()` method, which returns the value of the last element that satisfies the
        predicate (rather than its index)
        
        :param predicate: A function to execute for each element in the array. It should return a truthy value to
                          indicate a matching element has been found.
                          The function is called with the following arguments:
                          `element`: The current element being processed in the array.
                          `index`: The index of the current element being processed in the array.
                          `array`: The array the method was called upon.
        :type predicate: Union[Predicate, Callable[[T, Optional[int], Optional[List[T]]], bool]]
        :returns: the index of the last (highest-index) element in the array that passes the test. Otherwise -1 if
                  no matching element is found.
        :rtype: int
        """
        
        predicate = ArrayHelper.__setup_predicate(predicate)
        reversed_arr = ArrayHelper(self[::-1])
        i = reversed_arr.find_index(predicate)
        if i == -1:
            return -1
        return len(self) - i - 1
    
    def index_of(self, search_element: T, from_index: Optional[int] = 0) -> int:
        """The `index_of()` method returns the first index at which a given element can be found in the array, or -1
        if it is not present.
        
        :param search_element: Element to locate in the array.
        :type search_element: T
        :param from_index: Zero-based index at which to start searching
        :type from_index: Optional[int]
        :returns: The first index of the element in the array; -1 if not found.
        :rtype: int
        """
        
        if not self.includes(search_element):
            return -1
        if from_index < 0:
            from_index += len(self)
        if from_index < len(self) * -1:
            from_index = 0
        if from_index >= len(self):
            return -1
        return self.find_index(lambda v, i: v == search_element and i >= from_index)
    
    def last_index_of(self, search_element: T, from_index: Optional[int] = None) -> int:
        """The `last_index_of()` method returns the last index at which a given element can be found in the array, or -1
        if it is not present. The array is searched backwards, starting at `fromIndex`.
        
        :param search_element: Element to locate in the array.
        :type search_element: T
        :param from_index: Zero-based index at which to start searching backwards
        :type from_index: Optional[int]
        :returns: the last index of the element in the array; -1 if not found.
        :rtype: int
        """
        
        if not self.includes(search_element):
            return -1
        if from_index is None or from_index >= len(self):
            from_index = len(self) - 1
        if from_index < len(self) * -1:
            return -1
        if from_index < 0:
            from_index += len(self)
        return self.find_last_index(lambda v, i: v == search_element and i <= from_index)
    
    @overload
    def filter(self, predicate: Callable[[T, Optional[int], Optional[List[T]]], bool]) -> ArrayHelper:
        ...
    
    @overload
    def filter(self, predicate: Predicate) -> ArrayHelper:
        ...

    def filter(self, predicate: Union[Predicate, Callable[[T, Optional[int], Optional[List[T]]], bool]]) -> ArrayHelper:
        """The `filter()` method creates a shallow copy of a portion of a given array, filtered down to just the
        elements from the given array that pass the test implemented by the predicate.
        
        :param predicate: A function to execute for each element in the array. It should return a truthy value to
                          indicate a matching element has been found.
                          The function is called with the following arguments:
                          `element`: The current element being processed in the array.
                          `index`: The index of the current element being processed in the array.
                          `array`:The array the method was called upon.
        :type predicate: Union[Predicate, Callable[[T, Optional[int], Optional[List[T]]], bool]]
        :returns: a shallow copy of a portion of the given array, filtered down to just the elements from the given
                  array that pass the test implemented by the predicate. If no elements pass the test, an empty array
                  will be returned.
        :rtype: ArrayHelper
        """
        
        predicate = ArrayHelper.__setup_predicate(predicate)
        filtered = ArrayHelper()
        for i, v in enumerate(self):
            if predicate.call(v, i, self):
                filtered.append(v)
        return filtered
    
    def flat(self, depth: Optional[int] = 1) -> ArrayHelper:
        """The `flat()` method creates a new array with all sub-array elements concatenated into it recursively up to
        the specified depth
        
        :param depth: The depth level specifying how deep a nested array structure should be flattened. Defaults to 1.
        :type depth: Optional[int]
        :returns: a new array with the sub-array elements concatenated into it
        :rtype: ArrayHelper
        """
        
        flattened = ArrayHelper()
        for v in self:
            if isinstance(v, list) and depth > 0:
                flattened += ArrayHelper(v).flat(depth - 1)
            else:
                flattened.append(v)
        return flattened
    
    @overload
    def flat_map(self, predicate: Callable[[T, Optional[int], Optional[List[T]]], Any]) -> ArrayHelper:
        ...
    
    @overload
    def flat_map(self, predicate: Predicate):
        ...
    
    def flat_map(self,
                 predicate: Union[Predicate, Callable[[T, Optional[int], Optional[List[T]]], Any]]) -> ArrayHelper:
        """The `flat_map()` method returns a new array formed by applying a given predicate to each element of the
        array, and then flattening the result by one level. It is identical to a `map()` followed by a `flat()` of
        depth 1 (`arr.map(...args).flat()`), but slightly more efficient than calling those two methods separately.
        
        :param predicate: A function to execute for each element in the array. It should return an array containing
                          new elements of the new array, or a single non-array value to be added to the new array.
                          The function is called with the following arguments:
                          `element`: The current element being processed in the array.
                          `index`: The index of the current element being processed in the array.
                          `array`:The array the method was called upon.
        :type predicate: Union[Predicate, Callable[[T, Optional[int], Optional[List[T]]], Any]]
        :returns: a new array with each element being the result of the predicate and flattened by a depth of 1.
        :rtype: ArrayHelper
        """
        
        predicate = ArrayHelper.__setup_predicate(predicate)
        return self.map(predicate).flat()
    
    @overload
    def map(self, predicate: Callable[[T, Optional[int], Optional[List[T]]], Any]) -> ArrayHelper:
        ...
    
    @overload
    def map(self, predicate: Predicate) -> ArrayHelper:
        ...
    
    def map(self, predicate: Union[Predicate, Callable[[T, Optional[int], Optional[List[T]]], Any]]) -> ArrayHelper:
        """The `map()` method creates an ew array populated with the results of calling a provided function on every
        element in the calling array.
        
        :param predicate: A function to execute for each element in the array. It should return an array containing
                          new elements of the new array, or a single non-array value to be added to the new array.
                          The function is called with the following arguments:
                          `element`: The current element being processed in the array.
                          `index`: The index of the current element being processed in the array.
                          `array`:The array the method was called upon.
        :type predicate: Union[Predicate, Callable[[T, Optional[int], Optional[List[T]]], Any]]
        :returns:
        :rtype: ArrayHelper
        """
        
        predicate = ArrayHelper.__setup_predicate(predicate)
        mapped = ArrayHelper()
        for i, v in enumerate(self):
            mapped.append(predicate.call(v, i, self))
        return mapped
    
    @overload
    def each(self, predicate: Callable[[T, Optional[int], Optional[List[T]]], None]) -> None:
        ...
    
    @overload
    def each(self, predicate: Predicate) -> None:
        ...
    
    def each(self, predicate: Union[Predicate, Callable[[T, Optional[int], Optional[List[T]]], None]]) -> None:
        """The `each()` method executes a provided function once for each array element.
        
        :param predicate: A function to execute for each element in the array. Its return value is discarded.
                          The function is called with the following arguments:
                          `element`: The current element being processed in the array.
                          `index`: The index of the current element being processed in the array.
                          `array`:The array the method was called upon.
        :type predicate: Union[Predicate, Callable[[T, Optional[int], Optional[List[T]]], None]]
        :returns: None
        :rtype: None
        """
        
        predicate = ArrayHelper.__setup_predicate(predicate)
        for i, v in enumerate(self):
            predicate.call(v, i, self)
    
    def includes(self, search_element: T, from_index=0) -> bool:
        return search_element in self[max(0, from_index):]
    
    @overload
    def reduce(self,
               predicate: Callable[[Acc, T, Optional[int], Optional[List[T]]], Any], initial_value: Acc = None) -> Any:
        ...
    
    @overload
    def reduce(self, predicate: Predicate, initial_value: Acc = None) -> Any:
        ...
    
    def reduce(self,
               predicate: Union[Predicate, Callable[[Acc, T, Optional[int], Optional[List[T]]], Any]],
               initial_value: Optional[Acc] = None) -> Any:
        """The `reduce()` method executes a user-supplied "reducer" callback function on each element of the array, in
        order, passing in the return value from the calculation on the preceding element. The final result of running
        the reducer across all elements of the array is a single value.
        
        The first time the callback is run there is no "return value of the previous calculation". If supplied, an
        initial value may be used in its place. Otherwise, the array element at index 0 is used as the initial value
        and iteration starts from the next element (index 1 instead of index 0).
        
        The reducer walks through the array element-by-element, at each step adding the current array value to the
        result from the previous step (this result is the running sum of all the previous steps) — until there is no
        more elements to add.
        
        :param predicate: A function to execute for each element in the array. Its return value becomes the value
                          of the `accumulator` parameter on the next invocation of `predicate`. For the last invocation,
                          the return value becomes the return value of `reduce()`.
                          The function is called with the following arguments:
                          `accumulator`: The value resulting from the previous call to `predicate`. On the first call,
                                         `initial_value` if specified, otherwise the value of `array[0]`
                          `current_value`: The value of the current element. On the first call, the value of `array[0]`
                                           if an `initial_value` was specified, otherwise the value of `array[1]`
                          `current_index`: The index position of `current_value` in the array. On first call, `0` if
                                           `initial_value` was specified, otherwise `1`.
                          `array`: The array the method was called upon.
        :type predicate: Union[Predicate, Callable[[Acc, T, Optional[int], Optional[List[T]]], Any]]
        :param initial_value: A value to which `accumulator` is initialized the first time the callback is called. If
                              `initial_value` is specified, `predicate` starts executing with the first value in the
                              array as `current_value`. If `initial_value` is *not* specified, `accumulator` is
                              initialized to the first value in the array, and `predicate` starts executing with the
                              second value in the array as `current_value`. In this case, if the array is empty (so that
                              there's no first value to return as `accumulator`), an error is thrown.
        :type initial_value: Optional[Acc]
        :returns: the value that results from running the "Reducer" callback function to completion over the array.
        :rtype: Any
        """
        
        predicate = ArrayHelper.__setup_predicate(predicate)
        start_index = 1 if initial_value is None else 0
        accumulator = self[0] if initial_value is None else initial_value
        for i, v in enumerate(self[start_index:]):
            accumulator = predicate.call(accumulator, v, i, self)
        return accumulator

    @overload
    def reduce_right(self,
                     predicate: Callable[[Acc, T, Optional[int], Optional[List[T]]], Any],
                     initial_value: Acc = None) -> Any:
        ...

    @overload
    def reduce_right(self, predicate: Predicate, initial_value: Acc = None) -> Any:
        ...
    
    def reduce_right(self,
                     predicate: Union[Predicate, Callable[[Acc, T, Optional[int], Optional[List[T]]], Any]],
                     initial_value: Optional[Acc] = None) -> Any:
        """The `reduce_right()` method applies a function against an accumulator and each value of the array
        (from right-to-left) to reduce it to a single value.
        
        See also `reduce()` for left-to-right.
        
        :param predicate: A function to execute for each element in the array. Its return value becomes the value
                          of the `accumulator` parameter on the next invocation of `predicate`. For the last invocation,
                          the return value becomes the return value of `reduce()`.
                          The function is called with the following arguments:
                          `accumulator`: The value resulting from the previous call to `predicate`. On the first call,
                                         `initial_value` if specified, otherwise the value of `array[0]`
                          `current_value`: The value of the current element. On the first call, the value of `array[0]`
                                           if an `initial_value` was specified, otherwise the value of `array[1]`
                          `current_index`: The index position of `current_value` in the array. On first call, `0` if
                                           `initial_value` was specified, otherwise `1`.
                          `array`: The array the method was called upon.
        :type predicate: Union[Predicate, Callable[[Acc, T, Optional[int], Optional[List[T]]], Any]]
        :param initial_value: Value to use as accumulator to the first call of the `predicate`. If no initial value is
                              supplied, the last element in the array will be used and skipped. Calling reduce or
                              reduce_right on an empty array without an initial value creates an `IndexError`.
        :type initial_value: Optional[Acc]
        :returns: the value that results from the reduction.
        :rtype: Any
        """
        
        return self.reverse().reduce(predicate, initial_value)
    
    def reverse(self) -> ArrayHelper:
        return ArrayHelper(self[::-1])

    @overload
    def every(self, predicate: Callable[[T, Optional[int], Optional[List[T]]], bool]) -> bool:
        ...

    @overload
    def every(self, predicate: Predicate) -> bool:
        ...
    
    def every(self, predicate: Union[Predicate, Callable[[T, Optional[int], Optional[List[T]]], bool]]) -> bool:
        """The `every()` method tests whether all elements in the array pass the test implemented by the predicate.
        It returns a boolean value.
        
        :param predicate: A function to execute for each element in the array. It should return a truthy to indicate
                          the element passes the test, and a falsy value otherwise.
                          The function is called with the following arguments:
                          `element`: The current element being processed in the array.
                          `index`: The index of the current element being processed in the array.
                          `array`: The array the method was called upon.
        :type predicate: Union[Predicate, Callable[[T, Optional[int], Optional[List[T]]], bool]]
        :returns: `True` if `predicate` returns a truthy value for every array element, otherwise `False`
        :rtype: bool
        """
        
        predicate = ArrayHelper.__setup_predicate(predicate)
        return all(predicate.call(v, i, self) for i, v in enumerate(self))

    @overload
    def some(self, predicate: Callable[[T, Optional[int], Optional[List[T]]], bool]) -> bool:
        ...

    @overload
    def some(self, predicate: Predicate) -> bool:
        ...
    
    def some(self, predicate: Union[Predicate, Callable[[T, Optional[int], Optional[List[T]]], bool]]) -> bool:
        """The `some()` method tests whether at least one element in the array passes the test implemented by the
        provided function. It returns True if, in the array, it finds an element for which the provided function returns
        True; otherwise it returns False. It doesn't modify the array.
        
        :param predicate: A function to execute for each element in the array. It should return a truthy to indicate
                          the element passes the test, and a falsy value otherwise.
                          The function is called with the following arguments:
                          `element`: The current element being processed in the array.
                          `index`: The index of the current element being processed in the array.
                          `array`: The array the method was called upon.
        :type predicate: Union[Predicate, Callable[[T, Optional[int], Optional[List[T]]], bool]]
        :returns: `True` if the callback function returns a truthy value for at least one element in the array,
                  otherwise `False`.
        :rtype: bool
        """
    
        predicate = ArrayHelper.__setup_predicate(predicate)
        return any(predicate.call(v, i, self) for i, v in enumerate(self))
    
    def shift(self) -> T:
        """The `shift()` method removes the first element from the array and returns that removed element. The method
        changes the length of the array.
        
        :returns: the removed element from the array; None if the array is empty
        :rtype: T
        """
        
        if len(self) == 0:
            return None
        v = self[0]
        self.__delitem__(0)
        return v
    
    def unshift(self, *values: T) -> int:
        """The `unshift()` method adds one or more elements to the beginning of an array and returns the new length
        of the array.
        
        :param values: The elements to add to the front of the array.
        :type values: T
        :returns: the new length of the array upon which the method was called
        :rtype: int
        """
        
        for i, v in enumerate(values):
            self.insert(i, v)
        return len(self)
    
    def slice(self, start: Optional[int] = None, end: Optional[int] = None) -> ArrayHelper:
        """The `slice()` method returns a shallow copy of a portion of an array into a new array object selected from
        `start` to `end` (`end` not included) where `start` and `end` represent the index of items in that array. The
        original array will not be modified.
        
        :param start: Zero-based index at which to start extraction
        :type start: Optional[int]
        :param end: Zero-based index at which to end extraction. `slice()` extracts up to but not including `end`.
        :type end: Optional[int]
        :returns: a new array containing the extracted elements.
        :rtype: ArrayHelper
        """
        
        if start is None or start < len(self) * -1:
            start = 0
        elif start >= len(self):
            return ArrayHelper()
        if end is None or end >= len(self):
            end = len(self)
        elif end < 0:
            end += len(self)
        elif end < len(self) * -1:
            end = 0
        return ArrayHelper(self[start:end])
    
    def splice(self, start: int = 0, delete_count: Optional[int] = None, *items: T) -> ArrayHelper:
        """The `splice()` method changes the contents of an array by removing or replacing existing elements and/or
        adding new elements in place. To access part of an array without modifying it, see `slice()`.
        
        :param start: Zero-based index at which to start changing the array.
        :type start: int
        :param delete_count: An integer indicating the number of elements in the array to remove from `start`.
        :type delete_count: Optional[int]
        :param items: The elements to add to the array, beginning from `start`.
        :type items: T
        :returns: an array containing the deleted elements. If only one element is removed, an array of one element is
                  returned. If no elements are removed, an empty array is returned.
        :rtype ArrayHelper
        """
        
        if delete_count is None or delete_count >= len(self[start:]):
            delete_count = len(self[start:])
        end = start + delete_count
        deleted = self[start:end]
        self[start:end] = items
        return ArrayHelper(deleted)
    
    def __add__(self, other: list) -> ArrayHelper:
        if isinstance(other, list):
            return ArrayHelper(self + other)
        raise Exception(f'Cannot add {type(other)} to ArrayHelper')
