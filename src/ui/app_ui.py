#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application UI
-------------
User interface for the cryptocurrency trade simulator.

"""

import tkinter as tk
from tkinter import ttk
import logging
import threading
import time

class ApplicationUI:
    """User interface for the cryptocurrency trade simulator."""
    
    def __init__(self, ws_handler):
        """
        Initialize the application UI.
        
        Args:
            ws_handler: WebSocket handler instance
        """
        self.ws_handler = ws_handler
        self.root = None
        self.logger = logging.getLogger(__name__)
        
    def setup_ui(self):
        """Set up the user interface components."""
        self.root = tk.Tk()
        self.root.title("Cryptocurrency Trade Simulator")
        self.root.geometry("1200x800")
        
        # Create main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create left panel (input parameters)
        left_frame = ttk.LabelFrame(main_frame, text="Input Parameters", padding="10")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Create right panel (output values)
        right_frame = ttk.LabelFrame(main_frame, text="Output Values", padding="10")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Add input fields (placeholders)
        ttk.Label(left_frame, text="Asset:").grid(row=0, column=0, sticky=tk.W, pady=5)
        ttk.Entry(left_frame).grid(row=0, column=1, sticky=tk.W, pady=5)
        
        ttk.Label(left_frame, text="Order Type:").grid(row=1, column=0, sticky=tk.W, pady=5)
        ttk.Combobox(left_frame, values=["Market", "Limit"]).grid(row=1, column=1, sticky=tk.W, pady=5)
        
        ttk.Label(left_frame, text="Quantity:").grid(row=2, column=0, sticky=tk.W, pady=5)
        ttk.Entry(left_frame).grid(row=2, column=1, sticky=tk.W, pady=5)
        
        ttk.Label(left_frame, text="Fee Tier:").grid(row=3, column=0, sticky=tk.W, pady=5)
        ttk.Combobox(left_frame, values=["VIP 0", "VIP 1", "VIP 2"]).grid(row=3, column=1, sticky=tk.W, pady=5)
        
        # Add output fields (placeholders)
        ttk.Label(right_frame, text="Slippage:").grid(row=0, column=0, sticky=tk.W, pady=5)
        ttk.Label(right_frame, text="0.00").grid(row=0, column=1, sticky=tk.W, pady=5)
        
        ttk.Label(right_frame, text="Fees:").grid(row=1, column=0, sticky=tk.W, pady=5)
        ttk.Label(right_frame, text="0.00").grid(row=1, column=1, sticky=tk.W, pady=5)
        
        ttk.Label(right_frame, text="Market Impact:").grid(row=2, column=0, sticky=tk.W, pady=5)
        ttk.Label(right_frame, text="0.00").grid(row=2, column=1, sticky=tk.W, pady=5)
        
        ttk.Label(right_frame, text="Latency (ms):").grid(row=3, column=0, sticky=tk.W, pady=5)
        ttk.Label(right_frame, text="0").grid(row=3, column=1, sticky=tk.W, pady=5)
        
        ttk.Label(right_frame, text="Net Cost:").grid(row=4, column=0, sticky=tk.W, pady=5)
        ttk.Label(right_frame, text="0.00").grid(row=4, column=1, sticky=tk.W, pady=5)
        
        # Add simulate button
        ttk.Button(main_frame, text="Simulate Trade").pack(pady=10)
        
        self.logger.info("UI setup complete")
        
    def run(self):
        """Run the application."""
        self.setup_ui()
        
        # Start WebSocket connection in a separate thread
        ws_thread = threading.Thread(target=self.ws_handler.connect)
        ws_thread.daemon = True
        ws_thread.start()
        
        self.logger.info("Starting UI main loop")
        self.root.mainloop()