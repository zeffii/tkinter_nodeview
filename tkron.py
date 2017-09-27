import tkinter
top = tkinter.Tk()

socket_types = {
    'vector': {'color': 'orange'},
    'topo': {'color': 'yellow'},
    'matrix': {'color': '#aaeeff'}
}

def draw_node(cv, props, name):
    locx, locy = props['loc']
    dimx, dimy = props['dims']
    tid = cv.create_rectangle(locx, locy, locx+dimx, locy+dimy, fill="#aaeeee")

    name_height = 16
    sock_dims = 4
    inputs_y_offs = 18
    inputs_y_dist = 10
    text_x_bump = 4
    socket_text_x_bump = 12
    socket_text_y_bump = 4
    cv.create_rectangle(locx, locy, locx + dimx, locy + name_height, fill="#eeeeee")
    cv.create_text(locx+text_x_bump, locy+8, text=name, anchor=tkinter.W)

    # inputs
    for nidx, socket_data in enumerate(props['inputs']):
        sock_loc_x = locx - sock_dims
        sock_loc_y = locy + inputs_y_offs + (inputs_y_dist * nidx)
        cv.create_oval(
            sock_loc_x, sock_loc_y, sock_loc_x + (sock_dims*2), sock_loc_y + (sock_dims*2),
            fill=socket_types[socket_data['type']]['color']
        )
        cv.create_text(
            sock_loc_x + socket_text_x_bump, sock_loc_y + socket_text_y_bump, 
            text=socket_data['name'], anchor=tkinter.W)

    # outputs
    node_width = locx + dimx
    socket_text_negx_bump = 4
    for nidx, socket_data in enumerate(props['outputs']):
        sock_loc_x = node_width - sock_dims
        sock_loc_y = locy + inputs_y_offs + (inputs_y_dist * nidx)
        cv.create_oval(
            sock_loc_x, sock_loc_y, sock_loc_x + (sock_dims*2), sock_loc_y + (sock_dims*2),
            fill=socket_types[socket_data['type']]['color']
        )
        cv.create_text(
            sock_loc_x - socket_text_negx_bump, sock_loc_y + socket_text_y_bump, 
            text=socket_data['name'], anchor=tkinter.E)


    return tid


nodes = {
    "node1": {
        'loc': (50, 30), 'dims': (100, 130), 
        'inputs': (
            {'type': 'vector', 'name': 'Verts'}, 
            {'type': 'matrix', 'name': 'Matrix'}
        ), 
        'outputs': (
            {'type': 'vector', 'name': 'Verts'}, 
            {'type': 'topo', 'name': 'Edges'}
        )
    },
    "node2": {
        'loc': (110, 60), 'dims': (100, 130), 
        'inputs': (
            {'type': 'vector', 'name': 'Verts'}, 
            {'type': 'topo', 'name': 'Edges'}
        ),
        'outputs': (
            {'type': 'vector', 'name': 'Verts'}, 
            {'type': 'topo', 'name': 'Edges'}
        )
    },
    "node3": {
        'loc': (267, 80), 'dims': (100, 130), 
        'inputs': (
            {'type': 'vector', 'name': 'Verts'}, 
            {'type': 'topo', 'name': 'Faces'},
            {'type': 'matrix', 'name': 'Matrix'}
        ),
        'outputs': (
            {'type': 'vector', 'name': 'Verts'}, 
            {'type': 'topo', 'name': 'Edges'}
        )
    }
}

w = tkinter.Canvas ( top, bg="#2366AA", height=540, width=610)
w.pack(expand=tkinter.YES, fill=tkinter.BOTH)


for n in sorted(nodes.keys()):
    draw_node(w, props=nodes[n], name=n)

top.mainloop()