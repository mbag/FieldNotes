## What is Mixin class?

Mixin class is kind-of, sort-of not really a fully functional class on it's own.
For example 

```
class HelloMixin(object):
    def hello(self):
        return self.first

class WorldMixin(object):
    def world(self):
        return self.second
```

As you might see, if you created instance of any of these two classes,
 a call to hello() or world() methods would fail AttributeError.
This happens because self.first and self.second are not defined here. On first look this might seem as implementation error.
Why would you create class that cannot 

Lets look at the scenario when this might come handy.
Lets say you have mutliple classses in your project, some of them have common properties, so it makes sense to have parent class(es) from which they inherit common interface.
However, there are classes that should have a similar/same method, but are not logically related. It makes no sense to inherit from the same parent, just to get this one method.
Furthermore, adding rarely used methods to the parent class only bloats up the parent class, and adds to the complexity when multiple inheritance comes into mix.
 Of course, you could just implement same method on every class that needs it. 
This violates DRY principle and complicates changes and development down the road.

Enter mixin class. As the name suggest, you can **mix in** some functionality into your child class by inheriting from mixin class.

Lets return to the example above. As I mentioned, instances of classes HelloMixin and WorldMixin cannot be created directly, since they to lack *first* and *second* attribute respectively. However, if your child class has everything mixin needs to wrok properly, methods from mixin will work.

```
class HelloWorld(HelloMixin, WorldMixin):
    def __init__(self):
        self.first = 'Hello'
        self.second = 'World!'
```

Now, if you create instance of HelloWorld and call hello() and world() methods, it works just as it was expected.
```
>>> hw = HelloWorld()
>>> hw.hello() + ' ' + hw.world()
'Hello World!'
```

When it comes to order in which class should inherit from mixins, you need to put mixin classes before any other parent classes. By other classes I mean classes that can stand on their own, or ABCs.

This was of course, just a trivial example to ilustrate and introduce mixin pattern. 
In the real world you need to make sure you understand what are the assumptions of mixin class makes that you plan to use.
You can fail gloriously, if you call method or function from mixin, but don't have everything it needs to work properly :)

