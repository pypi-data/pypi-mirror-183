import unittest

from array_helpers import ArrayHelper, Predicate


class TestArrayHelpers(unittest.TestCase):
    def setUp(self):
        self.helper = ArrayHelper([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.boolean_lambda_one = lambda x: x == 2
        self.boolean_predicate_one = Predicate(lambda x: x == 2)
        self.boolean_lambda_two = lambda x: x % 2 == 0
        self.boolean_predicate_two = Predicate(lambda x: x % 2 == 0)
    
    def test_find(self):
        self.assertEqual(self.helper.find(self.boolean_lambda_one), 2)
        self.assertNotEqual(self.helper.find(self.boolean_lambda_two), 4)
        
        self.assertEqual(self.helper.find(self.boolean_predicate_one), 2)
        self.assertNotEqual(self.helper.find(self.boolean_predicate_two), 4)
    
    def test_find_index(self):
        self.assertEqual(self.helper.find_index(self.boolean_lambda_one), 1)
        self.assertNotEqual(self.helper.find_index(self.boolean_lambda_two), 3)
        
        self.assertEqual(self.helper.find_index(self.boolean_predicate_one), 1)
        self.assertNotEqual(self.helper.find_index(self.boolean_predicate_two), 3)
    
    def test_find_last(self):
        self.assertEqual(self.helper.find_last(self.boolean_lambda_one), 2)
        self.assertNotEqual(self.helper.find_last(self.boolean_lambda_two), 4)
        self.assertEqual(self.helper.find_last(self.boolean_lambda_two), 10)
        
        self.assertEqual(self.helper.find_last(self.boolean_predicate_one), 2)
        self.assertNotEqual(self.helper.find_last(self.boolean_predicate_two), 4)
        self.assertEqual(self.helper.find_last(self.boolean_predicate_two), 10)
    
    def test_find_last_index(self):
        self.assertEqual(self.helper.find_last_index(self.boolean_lambda_one), 1)
        self.assertNotEqual(self.helper.find_last_index(self.boolean_lambda_two), 3)
        self.assertEqual(self.helper.find_last_index(self.boolean_lambda_two), 9)
        
        self.assertEqual(self.helper.find_last_index(self.boolean_predicate_one), 1)
        self.assertNotEqual(self.helper.find_last_index(self.boolean_predicate_two), 3)
        self.assertEqual(self.helper.find_last_index(self.boolean_predicate_two), 9)
    
    def test_filter(self):
        self.assertEqual(self.helper.filter(self.boolean_lambda_one), [2])
        self.assertEqual(self.helper.filter(self.boolean_lambda_two), [2, 4, 6, 8, 10])
        
        self.assertEqual(self.helper.filter(self.boolean_predicate_one), [2])
        self.assertEqual(self.helper.filter(self.boolean_predicate_two), [2, 4, 6, 8, 10])
    
    def test_flat(self):
        helper = ArrayHelper([1, 2, [3, 4]])
        self.assertEqual(helper.flat(), [1, 2, 3, 4])
        
        helper.append([[5, 6]])
        self.assertEqual(helper.flat(), [1, 2, 3, 4, [5, 6]])
        self.assertEqual(helper.flat(2), [1, 2, 3, 4, 5, 6])
    
    def test_flat_map(self):
        helper = ArrayHelper([1, 2, 3, 4])
        self.assertEqual(helper.flat_map(lambda x: [x * 2]), [2, 4, 6, 8])
        self.assertEqual(helper.flat_map(lambda x: [[x * 2]]), [[2], [4], [6], [8]])
        
        helper = ArrayHelper([5, 4, -3, 20, 17, -33, -4, 18])
        pred = Predicate(lambda n: [] if n < 0 else ([n] if n % 2 == 0 else [n - 1, 1]))
        self.assertEqual(helper.flat_map(pred), [4, 1, 4, 20, 16, 1, 18])
    
    def test_map(self):
        helper = ArrayHelper([1, 4, 9])
        self.assertEqual(helper.map(lambda n: n ** 0.5), [1, 2, 3])
        
        helper = ArrayHelper([
            {'key': 1, 'value': 10},
            {'key': 2, 'value': 20},
            {'key': 3, 'value': 30},
        ])
        self.assertEqual(helper.map(lambda v: {v['key']: v['value']}), [{1: 10}, {2: 20}, {3: 30}])
    
    def test_includes(self):
        helper = ArrayHelper([1, 2, 3, 4])
        self.assertTrue(helper.includes(3))

        helper = ArrayHelper([
            {'key': 1, 'value': 10},
            {'key': 2, 'value': 20},
            {'key': 3, 'value': 30},
        ])
        self.assertTrue(helper.includes({'key': 2, 'value': 20}))
        self.assertFalse(helper.includes({'key': 1, 'value': 20}))
    
    def test_reduce(self):
        helper = ArrayHelper([15, 16, 17, 18, 19])
        self.assertEqual(helper.reduce(lambda accumulator, current_value: accumulator + current_value, 10), 95)
        
        helper = ArrayHelper([
            {'x': 1}, {'x': 2}, {'x': 3}
        ])
        self.assertEqual(helper.reduce(lambda accumulator, current_value: accumulator + current_value['x'], 0), 6)
        
        helper = ArrayHelper(['Alice', 'Bob', 'Tiff', 'Bruce', 'Alice'])
        
        def name_counter(all_names, name):
            current_count = all_names[name] if name in all_names else 0
            return {**all_names, name: current_count + 1}
        
        self.assertEqual(helper.reduce(name_counter, {}), {'Alice': 2, 'Bob': 1, 'Tiff': 1, 'Bruce': 1})
        
        helper = ArrayHelper([
            {'name': 'Alice', 'age': 21},
            {'name': 'Max', 'age': 20},
            {'name': 'Jane', 'age': 20},
        ])
        
        def group_by(prop: str):
            def fn(accumulator, obj):
                key = obj[prop]
                cur_group = accumulator[key] if key in accumulator else []
                
                return {**accumulator, key: [*cur_group, obj]}
            
            return fn
        
        self.assertEqual(
            helper.reduce(group_by('age'), {}),
            {21: [{'name': 'Alice', 'age': 21}], 20: [{'name': 'Max', 'age': 20}, {'name': 'Jane', 'age': 20}]})
        helper.append({'name': 'Max', 'age': 53})
        self.assertEqual(
            helper.reduce(group_by('name'), {}),
            {'Alice': [{'name': 'Alice', 'age': 21}],
             'Max': [{'name': 'Max', 'age': 20}, {'name': 'Max', 'age': 53}],
             'Jane': [{'name': 'Jane', 'age': 20}]})
    
    def test_reduce_right(self):
        helper = ArrayHelper(['1', '2', '3', '4', '5'])
        self.assertEqual(helper.reduce_right(lambda prev, cur: prev + cur), '54321')
    
    def test_every(self):
        is_big_enough = Predicate(lambda n: n >= 10)
        helper = ArrayHelper([12, 5, 8, 130, 44])
        self.assertFalse(helper.every(is_big_enough))
        helper[1:3] = [54, 18]
        self.assertTrue(helper.every(is_big_enough))
        
        is_subset = Predicate(lambda arr1, arr2: arr2.every(lambda n: arr1.includes(n)))
        main = ArrayHelper([1, 2, 3, 4, 5, 6, 7])
        subset = ArrayHelper([5, 7, 6])
        self.assertTrue(is_subset.call(main, subset))
        subset.splice(1, 2, 8, 7)
        self.assertFalse(is_subset.call(main, subset))
    
    def test_some(self):
        helper = ArrayHelper([2, 5, 8, 1, 4])
        self.assertFalse(helper.some(lambda n: n > 10))
        helper[0] = 12
        self.assertTrue(helper.some(lambda n: n > 10))
    
    def test_shit(self):
        helper = ArrayHelper(['angel', 'clown', 'mandarin', 'sturgeon'])
        shifted = helper.shift()
        self.assertEqual(shifted, 'angel')
        self.assertEqual(helper, ['clown', 'mandarin', 'sturgeon'])
    
    def test_unshift(self):
        helper = ArrayHelper([1, 2, 3])
        new_length = helper.unshift(4, 5)
        self.assertEqual(helper, [4, 5, 1, 2, 3])
        self.assertEqual(len(helper), new_length)
    
    def test_slice(self):
        helper = ArrayHelper(['Banana', 'Orange', 'Lemon', 'Apple', 'Mango'])
        self.assertEqual(helper.slice(1, 3), ['Orange', 'Lemon'])
        self.assertEqual(helper.slice(-3), ['Lemon', 'Apple', 'Mango'])
        self.assertEqual(helper.slice(-3, 2), [])
    
    def test_splice(self):
        helper = ArrayHelper(['angel', 'clown', 'mandarin', 'sturgeon'])
        removed = helper.splice(2, 0, 'drum')
        self.assertEqual(helper, ['angel', 'clown', 'drum', 'mandarin', 'sturgeon'])
        self.assertEqual(removed, [])
        
        removed = helper.splice(3, 1)
        self.assertEqual(helper, ['angel', 'clown', 'drum', 'sturgeon'])
        self.assertEqual(removed, ['mandarin'])
        
        removed = helper.splice(2, 1, 'trumpet')
        self.assertEqual(helper, ['angel', 'clown', 'trumpet', 'sturgeon'])
        self.assertEqual(removed, ['drum'])
        
        removed = helper.splice(0, 2, 'parrot', 'anemone', 'blue')
        self.assertEqual(helper, ['parrot', 'anemone', 'blue', 'trumpet', 'sturgeon'])
        self.assertEqual(removed, ['angel', 'clown'])
        
        removed = helper.splice(-2, 1)
        self.assertEqual(helper, ['parrot', 'anemone', 'blue', 'sturgeon'])
        self.assertEqual(removed, ['trumpet'])
        
        removed = helper.splice(2)
        self.assertEqual(helper, ['parrot', 'anemone'])
        self.assertEqual(removed, ['blue', 'sturgeon'])


if __name__ == '__main__':
    unittest.main()
