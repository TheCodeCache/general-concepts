# General Comparator Implementation:

```java
// save this code as Comparison.java
/**
 * Refer to class `GeneralComparator` for generic comparator implementation
 *
 * Caution: this code will be documented soon, though it is readable enough to walk-through.
 */
package com.example.samples.collection;

import java.lang.reflect.InvocationTargetException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.Stream;

class Person {

	private String name;
	private int age;
	private float salary;
	private String city;
	private Float point;

	public Person(String name, int age, float salary, String city, Float point) {
		super();
		this.name = name;
		this.age = age;
		this.salary = salary;
		this.city = city;
		this.point = point;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		this.age = age;
	}

	public float getSalary() {
		return salary;
	}

	public void setSalary(float salary) {
		this.salary = salary;
	}

	public String getCity() {
		return city;
	}

	public void setCity(String city) {
		this.city = city;
	}

	public Float getPoint() {
		return point;
	}

	public void setPoint(Float point) {
		this.point = point;
	}

	@Override
	public String toString() {
		return "Person [name=" + name + ", age=" + age + ", salary=" + salary + ", city=" + city + ", point=" + point
				+ "]";
	}
}

class PersonComparator implements Comparator<Person> {

	@Override
	public int compare(Person o1, Person o2) {

		if (o1.getName().equals(o2.getName()))
			if (o1.getAge() == o2.getAge())
				if (o1.getSalary() == o2.getSalary())
					return 0;
				else
					return o1.getSalary() > o2.getSalary() ? 1 : -1;
			else
				return o1.getAge() > o2.getAge() ? 1 : -1;
		else
			return o1.getName().compareTo(o2.getName());
	}
}

class NameComparator implements Comparator<Person> {

	@Override
	public int compare(Person o1, Person o2) {
		return o1.getName().compareTo(o2.getName());
	}
}

class AgeComparator implements Comparator<Person> {

	@Override
	public int compare(Person o1, Person o2) {
		return Integer.compare(o1.getAge(), o2.getAge());
	}
}

class SalaryComparator implements Comparator<Person> {

	@Override
	public int compare(Person o1, Person o2) {
		return Float.compare(o1.getSalary(), o2.getSalary());
	}
}

class ChainedComparator implements Comparator<Person> {

	private List<Comparator<Person>> list;

	public ChainedComparator(Comparator<Person> c1, Comparator<Person> c2, Comparator<Person> c3) {
		list = Stream.of(c1, c2, c3).collect(Collectors.toList());
	}

	@Override
	public int compare(Person o1, Person o2) {

		for (Comparator<Person> comp : list) {
			if (comp.compare(o1, o2) == 0)
				continue;
			else
				return comp.compare(o1, o2);
		}
		return 0;
	}
}

class GeneralComparator implements Comparator<Person> {

	private List<Comparator<Person>> list = new ArrayList<>();
	private Map<String, Class<?>> nameType = new HashMap<String, Class<?>>();

	public GeneralComparator(String[] propertyNames) {
		super();

		class PropertyComparator implements Comparator<Person> {

			private String property;
			private Class<?> type;

			public PropertyComparator(String property, Class<?> type) {
				this.property = property;
				this.type = type;
			}

			@Override
			public int compare(Person o1, Person o2) {
				try {

					if (type == java.lang.String.class) {

						/*
						 * PropertyDescriptor pd = new PropertyDescriptor(property, Person.class);
						 * 
						 * return ((String) pd.getReadMethod().invoke(o1)) .compareTo(((String)
						 * pd.getReadMethod().invoke(o2)));
						 */

						return castObject(String.class, o1.getClass().getMethod(getGetterMethod(property)).invoke(o1))
								.compareTo(castObject(String.class,
										o2.getClass().getMethod(getGetterMethod(property)).invoke(o2)));

						/*
						 * return ((String)
						 * o1.getClass().getMethod(getGetterMethod(property)).invoke(o1))
						 * .compareTo(((String)
						 * o1.getClass().getMethod(getGetterMethod(property)).invoke(o2)));
						 */
					} else if (type == int.class) {
						/*
						 * PropertyDescriptor pd = new PropertyDescriptor(property, Person.class);
						 * 
						 * return Integer.compare(((Integer) pd.getReadMethod().invoke(o1)), ((Integer)
						 * pd.getReadMethod().invoke(o2)));
						 */

						return castObject(Integer.class, o1.getClass().getMethod(getGetterMethod(property)).invoke(o1))
								.compareTo(castObject(Integer.class,
										o2.getClass().getMethod(getGetterMethod(property)).invoke(o2)));

						/*
						 * return Integer.compare( ((Integer)
						 * o1.getClass().getMethod(getGetterMethod(property)).invoke(o1)), ((Integer)
						 * o1.getClass().getMethod(getGetterMethod(property)).invoke(o2)));
						 */
					} else if (type == java.lang.Float.class || type == float.class) {
						/*
						 * PropertyDescriptor pd = new PropertyDescriptor(property, Person.class);
						 * 
						 * return Float.compare(((Float) pd.getReadMethod().invoke(o1)), ((Float)
						 * pd.getReadMethod().invoke(o2)));
						 */

						/*
						 * return castObject(float.class,
						 * type.getMethod(getGetterMethod(property)).invoke(o1)).compareTo(
						 * castObject(float.class,
						 * type.getMethod(getGetterMethod(property)).invoke(o2)));
						 */

						return castObject(java.lang.Float.class,
								o1.getClass().getMethod(getGetterMethod(property)).invoke(o1))
										.compareTo(castObject(java.lang.Float.class,
												o2.getClass().getMethod(getGetterMethod(property)).invoke(o2)));

						/*
						 * return Float.compare(((Float)
						 * o1.getClass().getMethod(getGetterMethod(property)).invoke(o1)), ((Float)
						 * o1.getClass().getMethod(getGetterMethod(property)).invoke(o2)));
						 */

					}

				} catch (IllegalArgumentException | SecurityException | IllegalAccessException
						| InvocationTargetException | NoSuchMethodException e) {
					e.printStackTrace();
				}
				return 0;
			}
		}

		Arrays.stream(Person.class.getDeclaredFields()).forEach(field -> {
			nameType.put(field.getName(), field.getType());
		});

		Arrays.stream(propertyNames)
				.forEach(property -> list.add(new PropertyComparator(property, nameType.get(property))));

	}

	@SuppressWarnings("unchecked")
	private <T> T castObject(Class<T> clazz, Object object) {
		return (T) object;
	}

	@Override
	public int compare(Person o1, Person o2) {

		for (Comparator<Person> comp : list) {
			if (comp.compare(o1, o2) == 0)
				continue;
			else
				return comp.compare(o1, o2);
		}
		return 0;
	}

	private String getGetterMethod(String propertyName) {
		// if boolean use "is" instead of "get"
		return "get" + propertyName.substring(0, 1).toUpperCase() + propertyName.substring(1);
	}
}

public class Comparison {

	public static void main(String[] args) {

		Person p1 = new Person("Naveen", 24, 5000, "rosera", 12.25F);
		Person p2 = new Person("Naveen", 25, 1000, "bangalore", 10.010F);
		Person p3 = new Person("Amit", 25, 6000, "patna", 12.25F);
		Person p4 = new Person("Amit", 25, 500, "rosera", 10.010F);
		Person p5 = new Person("Mano", 28, 1000, "bangalore", 0.01f);
		Person p6 = new Person("Mano", 28, 2000, "patna", 5.3f);
		Person p7 = new Person("Lok", 26, 1000, "nagpur", 0.01F);
		Person p8 = new Person("Manor", 24, 1000, "nagpur", 5.3f);

		Stream<Person> stream = Stream.of(p1, p2, p3, p4, p5, p6, p7, p8);
		List<Person> persons = stream.collect(Collectors.toList());

//		Collections.sort(persons, new PersonComparator());

		persons.forEach(System.out::println);

		Stream<Person> stream2 = Stream.of(p1, p2, p3, p4, p5, p6, p7, p8);
		List<Person> persons2 = stream2.collect(Collectors.toList());

		// Collections.sort(persons2,
		// new ChainedComparator(new SalaryComparator(), new NameComparator(), new
		// AgeComparator()));

		System.out.println();

		persons2.forEach(System.out::println);

		Stream<Person> stream3 = Stream.of(p1, p2, p3, p4, p5, p6, p7, p8);
		List<Person> persons3 = stream3.collect(Collectors.toList());

		Collections.sort(persons3, new GeneralComparator(new String[] { "point", "name", "salary", "age" }));

		System.out.println();

		persons3.forEach(System.out::println);
	}
}
```
