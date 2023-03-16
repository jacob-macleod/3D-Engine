var canvas = document.getElementById("screen");
var ctx = canvas.getContext("2d");

focal_length = 40

function find_point(focal_length, point, z) {
    new_point = (focal_length*point)/(focal_length+z)
    return new_point
}

// A list of points
// Lines are drawn between each block of two
// SO this essentially defines the vertices
// This seems like a horribly inefficient way to do define it, so I need to research alternatives
/*cube = [
    //x, y, z
    "60,20,20",   // Front bottom-left corner
    "90,20,20",   // Front bottom-right corner

    "90,60,20",   // Front top-right corner
    "80,60,20",   // Front top-left corner

    "90,60,20",   // Front top-right corner
    "90,20,20",   // Front bottom-right corner

    "60,60,20",   // Front top-left corner
    "60,20,20",   // Front bottom-left corner

    "60,20,60",   // Back bottom-left corner
    "90,20,60",   // Back bottom-right corner

    "90,60,60",   // Back top-right corner
    "60,60,60",   // Back top-left corner

    "90,60,60",   // Back top-right corner
    "90,20,60",   // Back bottom-right corner

    "60,60,60",   // Back top-left corner
    "60,20,60",   // Back bottom-left corner

    "90,60,20",   // Front top-right corner
    "90,60,60",   // Back top-right corner

    "60,60,20",   // Front top-left corner
    "60,60,60",   // Back top-left corner

    "60,20,20",   // Front bottom-left corner
    "60,20,60",   // Back bottom-left corner

    "90,20,20",   // Front bottom-right corner
    "90,20,60",   // Back bottom-right corner
]*/

cube = []

function create_cube_array() {
	for (line=0;line<coords.length;line++) {
		coordinate_pair = coords[line];
		item_1 = coordinate_pair.split("#")[0];
		item_2 = coordinate_pair.split("#")[1];
		
		// The coordinate is encapsulated with [], so we need to remove it
		item_1 = item_1.slice(1, -1);
		item_2 = item_2.slice(1, -1);

		// The coordinates also have spaces, so we need to remove them
		item_1 = item_1.replace(/\s/g, "");
		item_2 = item_2.replace(/\s/g, "");
		
		// Add the item to the array
		cube.push(item_1)
		cube.push(item_2)
	}
}

create_cube_array();


function render_cube() {
    // Draw the cube
    for (i=0;i<(cube.length); i++) {
        // If i = 0, 2, 4, 6, etc
        if ((i%2) == 0) {
            // Draw the line
            coords = cube[i].split(",")
            x1 = parseInt(coords[0])
            y1 = parseInt(coords[1])
            z1 = parseInt(coords[2])

            next_coords = cube[i+1].split(",")
            x2 = parseInt(next_coords[0])
            y2 = parseInt(next_coords[1])
            z2 = parseInt(next_coords[2])

            x1 = find_point(focal_length, x1, z1)
            y1 = find_point(focal_length, y1, z1)
            x2 = find_point(focal_length, x2, z2)
            y2 = find_point(focal_length, y2, z2)

            ctx.moveTo(x1, y1)
            ctx.lineTo(x2, y2);
            ctx.stroke();
        }
    }
}

render_cube()

// Increment all x coords in the array by num_of_steps
function move_horizontally(num_of_steps) {
    console.log(cube)
    newArr = []
    coords = []

    for (i=0;i<(cube.length); i++) {
        coords = cube[i].split(",")
        // Convert the x coord to a number, add num_of_steps to it, and turn it back into a string
        new_coordinate = parseInt(coords[0])
        new_coordinate = new_coordinate + num_of_steps
        coords[0] = (new_coordinate).toString()
        line = coords[0] + "," + coords[1] + "," + coords[2]
        newArr.push(line)
    }

    // Clear canvas
    ctx.fillStyle = "#FFFFFF";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.beginPath();

    cube = newArr

    // Redraw the cube
    render_cube()
    console.log(cube)
}

// Increment all y coords in the array by num_of_steps
function move_vertically(num_of_steps) {
    newArr = []
    coords = []

    for (i=0;i<(cube.length); i++) {
        coords = cube[i].split(",")
        // Convert the x coord to a number, add num_of_steps to it, and turn it back into a string
        new_coordinate = parseInt(coords[1])
        new_coordinate = new_coordinate + num_of_steps
        coords[1] = (new_coordinate).toString()
        line = coords[0] + "," + coords[1] + "," + coords[2]
        newArr.push(line)
    }

    // Clear canvas
    ctx.fillStyle = "#FFFFFF";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.beginPath();

    cube = newArr

    // Redraw the cube
    render_cube()
}

// Increment all z coords in the array by num_of_steps
function move_in_z_axis(num_of_steps) {
    console.log(cube);
    newArr = []
    coords = []

    for (i=0;i<(cube.length); i++) {
        coords = cube[i].split(",");
        // Convert the x coord to a number, add num_of_steps to it, and turn it back into a string
        new_coordinate = parseInt(coords[2]);
        new_coordinate = new_coordinate + num_of_steps;
        coords[2] = (new_coordinate).toString();
        line = coords[0] + "," + coords[1] + "," + coords[2];
        newArr.push(line)
    }

    // Clear canvas
    ctx.fillStyle = "#FFFFFF";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.beginPath();

    cube = newArr;

    // Redraw the cube
    render_cube();
    console.log(cube);
}
