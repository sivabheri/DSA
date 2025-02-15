
List:

	It is an sub-interface of  Collection Framework.
	It is used to store an ordered collection of elements.
	It can contain duplicates.

	It is implemented by classes such as: ArrayList, LikedList, Vector and Stack.

	Features:

		1. Order Preservation.
		2. Index-Based Access.
		3. Allows Duplicates.

ArrayList:

	It is a resizeable array.

	It is a Parameterised generic class which means we need to define what Type of elements we are storing.

	To import:

		import java.util.ArrayList

	To initialize:

		ArrayList< type > obj = new ArrayList<>();

						or

		List< type > obj = new ArrayList<>();


	Operations:

		1. To add:  list.add(1)

		2. To get an element: we can do with indexing.

				ele = list.get(index)

		3. To get size of list:  list.size()

		4. To iterate over a List:

				for (int x: list) : Here x is the element of the list not index.

		5. To check if element exists:

				list.contains( x ) : returns True/False

		6. To remove from a particular index:

				list.remove( index )

				if we do : list.remove( element ) : removes the first occerance of element

		7. To add an element at a particular index:

				list.add( index, element)

		8. To add a collection of items:  we use addall

				list.addall( collection_name )

		9. To empty the list: clear

				list.clear()

		10. To update an element at a particular index:

				list.set( index, new_element )

		11. To do shallow copy: clone()

		12. To get the index of the element: indexOf

				list.indexOf( element ) : returns index if exists else -1.

				last index: lastIndexOf( element ) 

		13. To remove all the elements of list2(collection) in list1:

				list1.removeall( list2 ) 

		14. To remove a particular index Range. : use removeRange

				list.removeRange( inclusive-from-index, exclusive-to-index)

		15. To get a portion of elements in index range : subList()

				new_list = list.subList( from-index, to-index )

		16. To convert anything to list:

				can be done during initailisation,

				ArrayList< int/type > list_obj = new ArrayList<>( collection_obj );

		17. To convert ArrayList to Array:

					// ArrayList to Array Conversion
        		int[] arr = list.stream().mapToInt(i -> i).toArray();

        18. To sort a List:

        			// import java.util.Collections
        		Collections.sort( List_obj )
        		