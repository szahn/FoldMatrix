## Fold matrix from bottom left to top right ##

### Examples
<img src="examples.png"/>

### Output
<b>2X2 MATRIX</b><br/>
ORIGINAL
<br/>
[1, 2]<br/>
[4, 3]
<br/><br/>
FOLDED<br/>
[1, 4]<br/>
[2, 3]

<b>3X3 MATRIX</b><br/>
ORIGINAL<br/>
[7, 5, 9]<br/>
[3, 4, 12]<br/>
[4, 6, 11]

FOLDED<br/>
[7, 3, 4]<br/>
[5, 4, 6]<br/>
[9, 12, 11]<br/>

<b>4X4 MATRIX</b><br/>
ORIGINAL<br/>
[1, 5, 6, 8]<br/>
[10, 12, 14, 56]<br/>
[4, 2, 1, 0]<br/>
[10, 19, 42, 7]<br/>

FOLDED<br/>
[1, 10, 4, 10]<br/>
[5, 12, 2, 19]<br/>
[6, 14, 1, 42]<br/>
[8, 56, 0, 7]<br/>

<b>5X5 MATRIX</b><br/>
ORIGINAL<br/>
[1, 5, 6, 8, 0]<br/>
[10, 12, 14, 56, 7]<br/>
[4, 2, 1, 0, 43]<br/>
[10, 19, 42, 7, 3]<br/>
[3, 66, 32, 12, 9]<br/>

FOLDED<br/>
[1, 10, 4, 10, 3]<br/>
[5, 12, 2, 19, 66]<br/>
[6, 14, 1, 42, 32]<br/>
[8, 56, 0, 7, 12]<br/>
[0, 7, 43, 3, 9]<br/>
