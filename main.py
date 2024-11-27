import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt

# Classes for Virtual Network Lab
class VirtualRouter:
    def __init__(self, name):
        self.name = name
        self.interfaces = {}
        self.routing_table = {}

    def configure_interface(self, interface, ip):
        self.interfaces[interface] = ip

    def add_route(self, destination, next_hop):
        self.routing_table[destination] = next_hop

    def forward_packet(self, packet):
        if packet.dst in self.routing_table:
            next_hop = self.routing_table[packet.dst]
            return next_hop
        else:
            return None


class Packet:
    def __init__(self, src, dst, data):
        self.src = src
        self.dst = dst
        self.data = data


class NetworkSimulation:
    def __init__(self):
        self.routers = {}
        self.topology = nx.Graph()

    def add_router(self, name):
        router = VirtualRouter(name)
        self.routers[name] = router
        self.topology.add_node(name)

    def connect_routers(self, router1_name, router2_name):
        if router1_name in self.routers and router2_name in self.routers:
            self.topology.add_edge(router1_name, router2_name)

    def visualize_topology(self):
        nx.draw(self.topology, with_labels=True, node_color="lightblue", node_size=3000)
        plt.show()

    def send_packet(self, src_router, packet):
        if src_router not in self.routers:
            return "Source router not found."

        current_router = src_router
        while current_router:
            next_hop = self.routers[current_router].forward_packet(packet)
            if next_hop:
                current_router = next_hop
            else:
                return f"Packet dropped at {current_router}."
        return f"Packet successfully delivered to {packet.dst}."


# GUI for Virtual Network Lab
class VirtualNetworkLabGUI:
    def __init__(self, root):
        self.network = NetworkSimulation()
        self.root = root
        self.root.title("Virtual Network Lab")
        self.root.geometry("400x600")  # Set window size

        # Background Color
        self.root.config(bg="#f0f0f0")

        # Main UI Layout
        self.title_label = tk.Label(root, text="Virtual Network Lab", font=("Arial", 18, 'bold'), bg="#f0f0f0")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Buttons for different actions
        self.add_router_button = self.create_button("Add Router", self.add_router_gui)
        self.connect_routers_button = self.create_button("Connect Routers", self.connect_routers_gui)
        self.configure_router_button = self.create_button("Configure Router", self.configure_router_gui)
        self.add_route_button = self.create_button("Add Route Entry", self.add_route_gui)
        self.visualize_topology_button = self.create_button("Visualize Topology", self.visualize_topology)
        self.send_packet_button = self.create_button("Send Packet", self.send_packet_gui)
        self.quit_button = self.create_button("Exit", root.quit)

    def create_button(self, text, command):
        button = tk.Button(self.root, text=text, command=command, width=25, font=("Arial", 12), bg="#005c39", fg="white", relief="flat")
        button.grid(pady=10)
        return button

    # GUI Actions
    def add_router_gui(self):
        def add_router_action():
            router_name = entry.get()
            if router_name:
                self.network.add_router(router_name)
                messagebox.showinfo("Success", f"Router {router_name} added!")
                window.destroy()
            else:
                messagebox.showerror("Error", "Router name cannot be empty.")

        window = self.create_popup_window("Add Router")
        tk.Label(window, text="Enter Router Name:", font=("Arial", 12)).pack(pady=5)
        entry = tk.Entry(window, font=("Arial", 12))
        entry.pack(pady=5)
        tk.Button(window, text="Add", command=add_router_action, font=("Arial", 12)).pack(pady=5)

    def connect_routers_gui(self):
        def connect_action():
            router1 = entry1.get()
            router2 = entry2.get()
            if router1 and router2:
                self.network.connect_routers(router1, router2)
                messagebox.showinfo("Success", f"Connected {router1} and {router2}")
                window.destroy()
            else:
                messagebox.showerror("Error", "Router names cannot be empty.")

        window = self.create_popup_window("Connect Routers")
        tk.Label(window, text="Enter First Router Name:", font=("Arial", 12)).pack(pady=5)
        entry1 = tk.Entry(window, font=("Arial", 12))
        entry1.pack(pady=5)
        tk.Label(window, text="Enter Second Router Name:", font=("Arial", 12)).pack(pady=5)
        entry2 = tk.Entry(window, font=("Arial", 12))
        entry2.pack(pady=5)
        tk.Button(window, text="Connect", command=connect_action, font=("Arial", 12)).pack(pady=5)

    def configure_router_gui(self):
        def configure_action():
            router_name = entry_router.get()
            interface = entry_interface.get()
            ip = entry_ip.get()
            if router_name and interface and ip:
                if router_name in self.network.routers:
                    self.network.routers[router_name].configure_interface(interface, ip)
                    messagebox.showinfo("Success", f"Configured {router_name} - {interface} with IP {ip}")
                    window.destroy()
                else:
                    messagebox.showerror("Error", "Router not found.")
            else:
                messagebox.showerror("Error", "All fields are required.")

        window = self.create_popup_window("Configure Router")
        tk.Label(window, text="Enter Router Name:", font=("Arial", 12)).pack(pady=5)
        entry_router = tk.Entry(window, font=("Arial", 12))
        entry_router.pack(pady=5)
        tk.Label(window, text="Enter Interface Name:", font=("Arial", 12)).pack(pady=5)
        entry_interface = tk.Entry(window, font=("Arial", 12))
        entry_interface.pack(pady=5)
        tk.Label(window, text="Enter IP Address:", font=("Arial", 12)).pack(pady=5)
        entry_ip = tk.Entry(window, font=("Arial", 12))
        entry_ip.pack(pady=5)
        tk.Button(window, text="Configure", command=configure_action, font=("Arial", 12)).pack(pady=5)

    def add_route_gui(self):
        def add_route_action():
            router_name = entry_router.get()
            destination = entry_destination.get()
            next_hop = entry_next_hop.get()
            if router_name and destination and next_hop:
                if router_name in self.network.routers:
                    self.network.routers[router_name].add_route(destination, next_hop)
                    messagebox.showinfo("Success", f"Added route to {destination} via {next_hop} on {router_name}")
                    window.destroy()
                else:
                    messagebox.showerror("Error", "Router not found.")
            else:
                messagebox.showerror("Error", "All fields are required.")

        window = self.create_popup_window("Add Route")
        tk.Label(window, text="Enter Router Name:", font=("Arial", 12)).pack(pady=5)
        entry_router = tk.Entry(window, font=("Arial", 12))
        entry_router.pack(pady=5)
        tk.Label(window, text="Enter Destination Network:", font=("Arial", 12)).pack(pady=5)
        entry_destination = tk.Entry(window, font=("Arial", 12))
        entry_destination.pack(pady=5)
        tk.Label(window, text="Enter Next Hop:", font=("Arial", 12)).pack(pady=5)
        entry_next_hop = tk.Entry(window, font=("Arial", 12))
        entry_next_hop.pack(pady=5)
        tk.Button(window, text="Add Route", command=add_route_action, font=("Arial", 12)).pack(pady=5)

    def visualize_topology(self):
        self.network.visualize_topology()

    def send_packet_gui(self):
        def send_packet_action():
            src_router = entry_src.get()
            src_ip = entry_src_ip.get()
            dst_ip = entry_dst_ip.get()
            data = entry_data.get()
            if src_router and dst_ip and data:
                packet = Packet(src_ip, dst_ip, data)
                result = self.network.send_packet(src_router, packet)
                messagebox.showinfo("Result", result)
                window.destroy()
            else:
                messagebox.showerror("Error", "All fields are required.")

        window = self.create_popup_window("Send Packet")
        tk.Label(window, text="Enter Source Router:", font=("Arial", 12)).pack(pady=5)
        entry_src = tk.Entry(window, font=("Arial", 12))
        entry_src.pack(pady=5)
        tk.Label(window, text="Enter Source IP:", font=("Arial", 12)).pack(pady=5)
        entry_src_ip = tk.Entry(window, font=("Arial", 12))
        entry_src_ip.pack(pady=5)
        tk.Label(window, text="Enter Destination IP:", font=("Arial", 12)).pack(pady=5)
        entry_dst_ip = tk.Entry(window, font=("Arial", 12))
        entry_dst_ip.pack(pady=5)
        tk.Label(window, text="Enter Packet Data:", font=("Arial", 12)).pack(pady=5)
        entry_data = tk.Entry(window, font=("Arial", 12))
        entry_data.pack(pady=5)
        tk.Button(window, text="Send", command=send_packet_action, font=("Arial", 12)).pack(pady=5)

    def create_popup_window(self, title):
        window = tk.Toplevel(self.root)
        window.title(title)
        window.geometry("300x300")
        window.config(bg="#f0f0f0")
        return window

if __name__ == "__main__":
    root = tk.Tk()
    gui = VirtualNetworkLabGUI(root)
    root.mainloop()
