#Example:
>> > value = bytearray([0xb9, 0x01, 0xef])
>> > value.hex()
'b901ef'
>> > value.hex(':')
'b9:01:ef'
>> > value.hex(':', 2)
'b9:01ef'
>> > value.hex(':', -2)
'b901:ef'
"""
pass

def index(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
"""
B.index(sub[, start[, end]]) -> int

Return
the
lowest
index in B
where
subsection
sub is found,
such
that
sub is contained
within
B[start, end].Optional
arguments
start and end
are
interpreted as in slice
notation.

Raises
ValueError
when
the
subsection is not found.
"""
return 0

def insert(self, *args, **kwargs): # real signature unknown
"""
Insert
a
single
item
into
the
bytearray
before
the
given
index.

index
The
index
where
the
value is to
be
inserted.
item
The
item
to
be
inserted.
"""
pass

def isalnum(self): # real signature unknown; restored from __doc__
"""
B.isalnum() -> bool

Return
True if all
characters in B
are
alphanumeric
and there is at
least
one
character in B, False
otherwise.
"""
return False

def isalpha(self): # real signature unknown; restored from __doc__
"""
B.isalpha() -> bool

Return
True if all
characters in B
are
alphabetic
and there is at
least
one
character in B, False
otherwise.
"""
return False

def isascii(self): # real signature unknown; restored from __doc__
"""
B.isascii() -> bool

Return
True if B is empty or all
characters in B
are
ASCII,
False
otherwise.
"""
return False

def isdigit(self): # real signature unknown; restored from __doc__
"""
B.isdigit() -> bool

Return
True if all
characters in B
are
digits
and there is at
least
one
character in B, False
otherwise.
"""
return False

def islower(self): # real signature unknown; restored from __doc__
"""
B.islower() -> bool

Return
True if all
cased
characters in B
are
lowercase and there is
at
least
one
cased
character in B, False
otherwise.
"""
return False

def isspace(self): # real signature unknown; restored from __doc__
"""
B.isspace() -> bool

Return
True if all
characters in B
are
whitespace
and there is at
least
one
character in B, False
otherwise.
"""
return False

def istitle(self): # real signature unknown; restored from __doc__
"""
B.istitle() -> bool

Return
True if B is a
titlecased
string and there is at
least
one
character in B, i.e.uppercase
characters
may
only
follow
uncased
characters and lowercase
characters
only
cased
ones.Return
False
otherwise.
"""
return False

def isupper(self): # real signature unknown; restored from __doc__
"""
B.isupper() -> bool

Return
True if all
cased
characters in B
are
uppercase and there is
at
least
one
cased
character in B, False
otherwise.
"""
return False

def join(self, *args, **kwargs): # real signature unknown
"""
Concatenate
any
number
of
bytes / bytearray
objects.

The
bytearray
whose
method is called is inserted in between
each
pair.

The
result is returned as a
new
bytearray
object.
"""
pass

def ljust(self, *args, **kwargs): # real signature unknown
"""
Return
a
left - justified
string
of
length
width.

Padding is done
using
the
specified
fill
character.
"""
pass

def lower(self): # real signature unknown; restored from __doc__
"""
B.lower() -> copy
of
B

Return
a
copy
of
B
with all ASCII characters converted to lowercase.
"""
pass

def lstrip(self, *args, **kwargs): # real signature unknown
"""
Strip
leading
bytes
contained in the
argument.

If
the
argument is omitted or None, strip
leading
ASCII
whitespace.
"""
pass

@staticmethod # known case
def maketrans(*args, **kwargs): # real signature unknown
"""
Return
a
translation
table
useable
for the bytes or bytearray translate method.

The
returned
table
will
be
one
where
each
byte in frm is mapped
to
the
byte
at
the
same
position in to.

The
bytes
objects
frm and to
must
be
of
the
same
length.
"""
pass

def partition(self, *args, **kwargs): # real signature unknown
"""
Partition
the
bytearray
into
three
parts
using
the
given
separator.

This
will
search
for the separator sep in the bytearray.If the separator is
found, returns
a
3 - tuple
containing
the
part
before
the
separator, the
separator
itself, and the
part
after
it as new
bytearray
objects.

If
the
separator is not found, returns
a
3 - tuple
containing
the
copy
of
the
original
bytearray
object and two
empty
bytearray
objects.
"""
pass

def pop(self, *args, **kwargs): # real signature unknown
"""
Remove and
return a
single
item
from B.

index
The
index
from where to

remove
the
item.
-1(the
default
value) means
remove
the
last
item.

If
no
index
argument is given, will
pop
the
last
item.
"""
pass

def remove(self, *args, **kwargs): # real signature unknown
"""
Remove
the
first
occurrence
of
a
value in the
bytearray.

value
The
value
to
remove.
"""
pass

def removeprefix(self, *args, **kwargs): # real signature unknown
"""
Return
a
bytearray
with the given prefix string removed if present.

If
the
bytearray
starts
with the prefix string, return
bytearray[len(prefix):].Otherwise,
return a
copy
of
the
original
bytearray.
"""
pass

def removesuffix(self, *args, **kwargs): # real signature unknown
"""
Return
a
bytearray
with the given suffix string removed if present.

If
the
bytearray
ends
with the suffix string and that suffix is not
empty,
return bytearray[:-len(suffix)].Otherwise,
return a
copy
of
the
original
bytearray.
"""
pass

def replace(self, *args, **kwargs): # real signature unknown
"""
Return
a
copy
with all occurrences of substring old replaced by new.

count
Maximum
number
of
occurrences
to
replace.
-1(the
default
value) means
replace
all
occurrences.

If
the
optional
argument
count is given, only
the
first
count
occurrences
are
replaced.
"""
pass

def reverse(self, *args, **kwargs): # real signature unknown
"""
Reverse
the
order
of
the
values in B in place.
"""
      pass

  def rfind(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
      """
B.rfind(sub[, start[, end]]) -> int

Return
the
highest
index in B
where
subsection
sub is found,
such
that
sub is contained
within
B[start, end].Optional
arguments
start and end
are
interpreted as in slice
notation.

Return - 1
on
failure.
"""
return 0

def rindex(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
"""
B.rindex(sub[, start[, end]]) -> int

Return
the
highest
index in B
where
subsection
sub is found,
such
that
sub is contained
within
B[start, end].Optional
arguments
start and end
are
interpreted as in slice
notation.

Raise
ValueError
when
the
subsection is not found.
"""
return 0

def rjust(self, *args, **kwargs): # real signature unknown
"""
Return
a
right - justified
string
of
length
width.

Padding is done
using
the
specified
fill
character.
"""
pass

def rpartition(self, *args, **kwargs): # real signature unknown
"""
Partition
the
bytearray
into
three
parts
using
the
given
separator.

This
will
search
for the separator sep in the bytearray, starting at the end.
If
the
separator is found, returns
a
3 - tuple
containing
the
part
before
the
separator, the
separator
itself, and the
part
after
it as new
bytearray
objects.

If
the
separator is not found, returns
a
3 - tuple
containing
two
empty
bytearray
objects and the
copy
of
the
original
bytearray
object.
"""
pass

def rsplit(self, *args, **kwargs): # real signature unknown
"""
Return
a
list
of
the
sections in the
bytearray, using
sep as the
delimiter.

sep
The
delimiter
according
which
to
split
the
bytearray.
None(the
default
value) means
split
on
ASCII
whitespace
characters
(space, tab,
return, newline, formfeed, vertical
tab).
maxsplit
Maximum
number
of
splits
to
do.
- 1(the
default
value) means
no
limit.

Splitting is done
starting
at
the
end
of
the
bytearray and working
to
the
front.
"""
pass

def rstrip(self, *args, **kwargs): # real signature unknown
"""
Strip
trailing
bytes
contained in the
argument.

If
the
argument is omitted or None, strip
trailing
ASCII
whitespace.
"""
pass

def split(self, *args, **kwargs): # real signature unknown
"""
Return
a
list
of
the
sections in the
bytearray, using
sep as the
delimiter.

sep
The
delimiter
according
which
to
split
the
bytearray.
None(the
default
value) means
split
on
ASCII
whitespace
characters
(space, tab,
return, newline, formfeed, vertical
tab).
maxsplit
Maximum
number
of
splits
to
do.
- 1(the
default
value) means
no
limit.
"""
pass

def splitlines(self, *args, **kwargs): # real signature unknown
"""
Return
a
list
of
the
lines in the
bytearray, breaking
at
line
boundaries.

Line
breaks
are
not included in the
resulting
list
unless
keepends is given and
true.
"""
pass

def startswith(self, prefix, start=None, end=None): # real signature unknown; restored from __doc__
"""
B.startswith(prefix[, start[, end]]) -> bool

Return
True if B
starts
with the specified prefix, False otherwise.
With optional start, test B beginning at that position.
With optional end, stop comparing B at that position.
prefix can also be a tuple of bytes to
try.
"""
return False

def strip(self, *args, **kwargs): # real signature unknown
"""
Strip
leading and trailing
bytes
contained in the
argument.

If
the
argument is omitted or None, strip
leading and trailing
ASCII
whitespace.
"""
pass

def swapcase(self): # real signature unknown; restored from __doc__
"""
B.swapcase() -> copy
of
B

Return
a
copy
of
B
with uppercase ASCII characters converted
to
lowercase
ASCII and vice
versa.
"""
pass

def title(self): # real signature unknown; restored from __doc__
"""
B.title() -> copy
of
B

Return
a
titlecased
version
of
B, i.e.ASCII
words
start
with uppercase
    characters, all
    remaining
    cased
    characters
    have
    lowercase.
"""
pass

def translate(self, *args, **kwargs): # real signature unknown
"""
Return
a
copy
with each character mapped by the given translation table.

table
Translation
table, which
must
be
a
bytes
object
of
length
256.

All
characters
occurring in the
optional
argument
delete
are
removed.
The
remaining
characters
are
mapped
through
the
given
translation
table.
"""
pass

def upper(self): # real signature unknown; restored from __doc__
"""
B.upper() -> copy
of
B

Return
a
copy
of
B
with all ASCII characters converted to uppercase.
"""
pass

def zfill(self, *args, **kwargs): # real signature unknown
"""
Pad
a
numeric
string
with zeros on the left, to fill a field of the given width.

The
original
string is never
truncated.
"""
pass

def __add__(self, *args, **kwargs): # real signature unknown
"""
Return
self + value.
"""
      pass

  def __alloc__(self): # real signature unknown; restored from __doc__
      """
B.__alloc__() -> int

Return
the
number
of
bytes
actually
allocated.
"""
return 0

def __contains__(self, *args, **kwargs): # real signature unknown
"""
Return
key in self.
"""
      pass

  def __delitem__(self, *args, **kwargs): # real signature unknown
      """
Delete
self[key].
"""
      pass

  def __eq__(self, *args, **kwargs): # real signatu
