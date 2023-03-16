"""
Read obj files, and use it to generate a list of points to draw between
"""

# Read an obj file and generate a list of vertices and faces
def read_obj(file) :
    # Define variables
    data = []
    vertices = ""
    faces = ""


    with open(file, "r") as file:
        for line in file:
            # Split each line by space
            line_data = line.split(" ")
            num_of_items = len(line_data)
            # If the data is a vertice
            if line_data[0] == "v" :
                # Add it to the string listing vertices
                vertices = vertices + line_data[1] + "," + line_data[2] + "," + line_data[3].replace('\n', '') + "#"
            elif line_data[0] == "f":
                # If the data is a face then add every face to the faces array
                for i in range(1, len(line_data) -1) :
                    faces = faces + line_data[i] + ","
                # For the final face item, don't add a comma on the end
                # Finish the section with a #
                # Also, remove any \n characters on the end
                faces = faces + line_data[len(line_data) - 1].replace('\n', '') + "#"
            
    data.append(vertices)
    data.append(faces)
    return data


def generate_coordinate_pairs(filename):
    coordinate_pairs = []
    with open(filename, 'r') as f:
        vertices = []
        for line in f:
            if line.startswith('v'):
                vertex = list(map(float, line.split()[1:]))
                vertices.append(vertex)
            elif line.startswith('f'):
                indices = list(map(int, line.split()[1:]))
                for i in range(len(indices)):
                    start = indices[i]
                    end = indices[(i+1)%len(indices)]
                    coordinate_pairs.append(f"{vertices[start-1]}#{vertices[end-1]}")
    return coordinate_pairs



