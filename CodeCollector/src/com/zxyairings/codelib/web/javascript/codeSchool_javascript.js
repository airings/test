/*

 *Now the Poplar Puzzle-makers have sent you a puzzle with a new set of functions to use on that puzzle. To display your overwhelming array and function expression mastery, alert the answer to the following question:

“What is obtained when the result of passing 9 into the fourth function of the puzzlers array is then passed into the function whose array index matches the result of passing 3 into the second function of the puzzlers array?”

To really impress them, the expression used in your alert should:

Use just one line of code.
Involve no manual calculation or hard-coded math on your part.
Use indices of arrays to access functions.
Use parentheses to pass in parameters to immediately-invoking functions.
 */
var puzzlers = [
  function(a) { return 8 * a - 10; },
  function(a) { return (a - 3) * (a - 3) * (a - 3); },
  function(a) { return a * a + 4; },
  function(a) { return a % 5; }
];

alert(puzzlers[puzzlers[1](3)](puzzlers[3](9)));


/*
The devs at Poplar Puzzles would like you to treat an array of functions like a Queue, 
passing the result of each function into the next until the Queue is empty. 
They’ve sent you the puzzlers Queue of functions, and the following instructions:
Build a function and assign it to a variable named applyAndEmpty.
The function should take in an input number and a queue of functions as parameters.
Using a for loop, call the functions in the queue in order with the input number, where the results of each function becomes the next function’s input.
Once done this loop, return from applyAndEmpty the final function’s result. Additionally, the queue should be empty at this point.
Lastly, call the applyAndEmpty function using the provided start variable and the puzzlers Queue as arguments, and alert the result.
*/

var puzzlers = [
                function(a) { return 8 * a - 10; },
                function(a) { return (a - 3) * (a - 3) * (a - 3); },
                function(a) { return a * a + 4; },
                function(a) { return a % 5; }
              ];
var start = 2;
var applyAndEmpty = function (input, queue) {
	  var length = queue.length;
	  for (var i = 0; i < length; i++) {
	    input = queue.shift()(input);
	  }
	  return input;
};
alert(applyAndEmpty(start, puzzlers));

/*
 * The Dev Girls need you to store each location so that a list of danger zones for each obstacle can be reported with every new warning.

Inside the warningMaker function:

Store each location in an array called zones.
Add each zone to the list string.
Report the list of danger zones with the alert message in this format:
Beware! There have been <obstacle> sightings in the Cove today!
<number> have been spotted at the <location>!
This is alert #<count> today for <obstacle> danger.
Current danger zones are:
<zone1>
<zone2>
<zone3>
...
 * 
 */
function warningMaker(obstacle) {
	  var count = 0;
	  var zones = [];
	  return function(number, location) {
	    count++;
	    var list = "";
	    // add each location to the zones array
	    zones.push(location);
	    // add each zone to the list string
			list = zones.join('\n');    
	    alert("Beware! There have been " + obstacle +
	          " sightings in the Cove today!\n" +
	          number + " have been spotted at the " +
	          location + "!\n" +
	          "This is alert #" + count +
	          " today for " + obstacle + " danger.\n" +
	          // finish the warning message here
	          "Current danger zones are:\n"+list
	    );
	  };
	}