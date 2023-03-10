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
cube = [
    //x, y, z
    "6,2,2",   // Front bottom-left corner
    "9,2,2",   // Front bottom-right corner

    "9,6,2",   // Front top-right corner
    "8,6,2",   // Front top-left corner

    "9,6,2",   // Front top-right corner
    "9,2,2",   // Front bottom-right corner

    "6,6,2",   // Front top-left corner
    "6,2,2",   // Front bottom-left corner

    "6,2,6",   // Back bottom-left corner
    "9,2,6",   // Back bottom-right corner

    "9,6,6",   // Back top-right corner
    "6,6,6",   // Back top-left corner

    "9,6,6",   // Back top-right corner
    "9,2,6",   // Back bottom-right corner

    "6,6,6",   // Back top-left corner
    "6,2,6",   // Back bottom-left corner

    "9,6,2",   // Front top-right corner
    "9,6,6",   // Back top-right corner

    "6,6,2",   // Front top-left corner
    "6,6,6",   // Back top-left corner

    "6,2,2",   // Front bottom-left corner
    "6,2,6",   // Back bottom-left corner

    "9,2,2",   // Front bottom-right corner
    "9,2,6",   // Back bottom-right corner
]

function render_cube() {
    // Draw the cube
    for (i=0;i<(cube.length); i++) {
        // If i = 0, 2, 4, 6, etc
        if ((i%2) == 0) {
            // Draw the line
            coords = cube[i].split(",")
            x1 = parseInt(coords[0]) * 100
            y1 = parseInt(coords[1]) * 100
            z1 = parseInt(coords[2]) * 100

            next_coords = cube[i+1].split(",")
            x2 = parseInt(next_coords[0]) * 100
            y2 = parseInt(next_coords[1]) * 100
            z2 = parseInt(next_coords[2]) * 100

            x1 = find_point(focal_length, x1, z1)
            y1 = find_point(focal_length, y1, z1)
            x2 = find_point(focal_length, x2, z2)
            y2 = find_point(focal_length, y2, z2)

            ctx.moveTo(x1, y1)
            ctx.lineTo(x2, y2);
            ctx.stroke();
            console.log(x1)
        }
    }
}

render_cube()

// Increment all x coords in the array by num_of_steps
function move_horizontally(num_of_steps) {
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
}