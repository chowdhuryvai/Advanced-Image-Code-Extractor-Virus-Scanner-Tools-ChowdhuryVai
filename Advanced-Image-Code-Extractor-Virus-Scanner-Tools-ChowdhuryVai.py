import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import os
import sys
import io
import struct
import hashlib
import re
from PIL import Image, ImageTk
import threading

class ChowdhuryVaiImageAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title("ChowdhuryVai - Advanced Image Code Extractor & Virus Scanner")
        self.root.geometry("1200x800")
        self.root.configure(bg='#0c0c0c')
        
        # Branding information
        self.brand_info = {
            "Telegram ID": "https://t.me/darkvaiadmin",
            "Telegram Channel": "https://t.me/windowspremiumkey", 
            "Website": "https://crackyworld.com/"
        }
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg='#0c0c0c')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Header
        header_frame = tk.Frame(main_frame, bg='#0c0c0c')
        header_frame.pack(fill='x', pady=(0, 20))
        
        title_label = tk.Label(
            header_frame, 
            text="CHOWDHURYVAI ADVANCED IMAGE ANALYZER",
            font=('Courier', 24, 'bold'),
            fg='#00ff00',
            bg='#0c0c0c'
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            header_frame,
            text="Professional Code Extraction & Security Analysis Tool",
            font=('Arial', 12),
            fg='#ff6600',
            bg='#0c0c0c'
        )
        subtitle_label.pack(pady=(5, 0))
        
        # Content frame
        content_frame = tk.Frame(main_frame, bg='#0c0c0c')
        content_frame.pack(fill='both', expand=True)
        
        # Left panel - Image and controls
        left_frame = tk.Frame(content_frame, bg='#1a1a1a', relief='ridge', bd=2)
        left_frame.pack(side='left', fill='both', expand=True, padx=(0, 10))
        
        # Image display area
        self.image_frame = tk.Frame(left_frame, bg='#000000', height=300)
        self.image_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.image_label = tk.Label(self.image_frame, text="No Image Selected", bg='#000000', fg='#ffffff')
        self.image_label.pack(expand=True)
        
        # Controls
        control_frame = tk.Frame(left_frame, bg='#1a1a1a')
        control_frame.pack(fill='x', padx=10, pady=10)
        
        # File selection
        file_frame = tk.Frame(control_frame, bg='#1a1a1a')
        file_frame.pack(fill='x', pady=5)
        
        tk.Button(
            file_frame, 
            text="📁 SELECT IMAGE", 
            command=self.select_image,
            bg='#0066cc',
            fg='white',
            font=('Arial', 10, 'bold'),
            relief='raised',
            bd=3
        ).pack(side='left', padx=(0, 10))
        
        self.file_path = tk.Entry(file_frame, width=50, font=('Arial', 10))
        self.file_path.pack(side='left', fill='x', expand=True)
        
        # Action buttons
        button_frame = tk.Frame(control_frame, bg='#1a1a1a')
        button_frame.pack(fill='x', pady=10)
        
        tk.Button(
            button_frame,
            text="🔍 EXTRACT CODE",
            command=self.start_analysis,
            bg='#00cc00',
            fg='white',
            font=('Arial', 11, 'bold'),
            relief='raised',
            bd=3,
            width=15
        ).pack(side='left', padx=5)
        
        tk.Button(
            button_frame,
            text="🛡️ SCAN FOR VIRUS",
            command=self.scan_for_virus,
            bg='#cc0000',
            fg='white',
            font=('Arial', 11, 'bold'),
            relief='raised',
            bd=3,
            width=15
        ).pack(side='left', padx=5)
        
        tk.Button(
            button_frame,
            text="🧹 CLEAR ALL",
            command=self.clear_all,
            bg='#666666',
            fg='white',
            font=('Arial', 11, 'bold'),
            relief='raised',
            bd=3,
            width=15
        ).pack(side='left', padx=5)
        
        # Progress bar
        self.progress = ttk.Progressbar(
            control_frame, 
            orient='horizontal', 
            length=100, 
            mode='indeterminate'
        )
        self.progress.pack(fill='x', pady=10)
        
        # Right panel - Results
        right_frame = tk.Frame(content_frame, bg='#1a1a1a', relief='ridge', bd=2)
        right_frame.pack(side='right', fill='both', expand=True, padx=(10, 0))
        
        # Results notebook
        self.notebook = ttk.Notebook(right_frame)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Extracted code tab
        code_frame = tk.Frame(self.notebook, bg='#1a1a1a')
        self.notebook.add(code_frame, text="📄 EXTRACTED CODE")
        
        self.code_text = scrolledtext.ScrolledText(
            code_frame, 
            bg='#000000', 
            fg='#00ff00',
            insertbackground='#00ff00',
            font=('Courier', 10),
            wrap=tk.WORD
        )
        self.code_text.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Analysis results tab
        analysis_frame = tk.Frame(self.notebook, bg='#1a1a1a')
        self.notebook.add(analysis_frame, text="🔍 ANALYSIS RESULTS")
        
        self.analysis_text = scrolledtext.ScrolledText(
            analysis_frame,
            bg='#000000',
            fg='#ffff00',
            insertbackground='#ffff00',
            font=('Arial', 10),
            wrap=tk.WORD
        )
        self.analysis_text.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Footer with branding
        footer_frame = tk.Frame(main_frame, bg='#0c0c0c')
        footer_frame.pack(fill='x', pady=(20, 0))
        
        for key, value in self.brand_info.items():
            brand_label = tk.Label(
                footer_frame,
                text=f"{key}: {value}",
                font=('Arial', 9),
                fg='#66ccff',
                bg='#0c0c0c',
                cursor='hand2'
            )
            brand_label.pack(pady=2)
            brand_label.bind('<Button-1>', lambda e, url=value: self.open_url(url))
        
        status_label = tk.Label(
            footer_frame,
            text="🔒 Professional Security Tool - Use Responsibly",
            font=('Arial', 10, 'italic'),
            fg='#ff3366',
            bg='#0c0c0c'
        )
        status_label.pack(pady=(10, 0))
    
    def open_url(self, url):
        import webbrowser
        webbrowser.open(url)
    
    def select_image(self):
        file_path = filedialog.askopenfilename(
            title="Select Image File",
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.bmp *.gif *.tiff"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            self.file_path.delete(0, tk.END)
            self.file_path.insert(0, file_path)
            self.display_image(file_path)
    
    def display_image(self, file_path):
        try:
            image = Image.open(file_path)
            image.thumbnail((400, 300))
            photo = ImageTk.PhotoImage(image)
            
            self.image_label.configure(image=photo)
            self.image_label.image = photo
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {str(e)}")
    
    def start_analysis(self):
        if not self.file_path.get():
            messagebox.showwarning("Warning", "Please select an image file first!")
            return
        
        self.progress.start()
        threading.Thread(target=self.analyze_image, daemon=True).start()
    
    def analyze_image(self):
        try:
            file_path = self.file_path.get()
            
            # Clear previous results
            self.code_text.delete(1.0, tk.END)
            self.analysis_text.delete(1.0, tk.END)
            
            # Extract hidden data
            extracted_data = self.extract_hidden_data(file_path)
            
            # Update UI in main thread
            self.root.after(0, self.update_results, extracted_data)
            
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", f"Analysis failed: {str(e)}"))
        finally:
            self.root.after(0, self.progress.stop)
    
    def extract_hidden_data(self, file_path):
        results = {
            'metadata': {},
            'hidden_strings': [],
            'suspicious_patterns': [],
            'file_info': {},
            'hex_data': ''
        }
        
        try:
            # Get file information
            file_size = os.path.getsize(file_path)
            results['file_info']['size'] = f"{file_size} bytes"
            
            # Calculate file hash
            file_hash = self.calculate_file_hash(file_path)
            results['file_info']['md5_hash'] = file_hash
            
            # Read image data
            with open(file_path, 'rb') as f:
                image_data = f.read()
            
            # Extract metadata
            results['metadata'] = self.extract_metadata(file_path)
            
            # Extract strings from binary data
            results['hidden_strings'] = self.extract_strings(image_data)
            
            # Look for suspicious patterns
            results['suspicious_patterns'] = self.find_suspicious_patterns(image_data)
            
            # Extract potential hidden code
            results['hex_data'] = self.extract_potential_code(image_data)
            
        except Exception as e:
            results['error'] = str(e)
        
        return results
    
    def calculate_file_hash(self, file_path):
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    def extract_metadata(self, file_path):
        metadata = {}
        try:
            with Image.open(file_path) as img:
                metadata['format'] = img.format
                metadata['mode'] = img.mode
                metadata['size'] = img.size
                
                # Extract EXIF data if available
                exif_data = img._getexif()
                if exif_data:
                    for tag_id, value in exif_data.items():
                        metadata[f'exif_{tag_id}'] = str(value)
        except:
            pass
        
        return metadata
    
    def extract_strings(self, data, min_length=4):
        strings = []
        try:
            # Extract ASCII strings
            pattern = b'[\\x20-\\x7e]{' + str(min_length).encode() + b',}'
            matches = re.findall(pattern, data)
            strings.extend(match.decode('ascii', errors='ignore') for match in matches)
        except:
            pass
        
        return strings
    
    def find_suspicious_patterns(self, data):
        suspicious = []
        
        # Common malicious code patterns
        patterns = [
            b'eval\\(',
            b'exec\\(',
            b'system\\(',
            b'base64_decode',
            b'Shellcode',
            b'cmd\\.exe',
            b'powershell',
            b'javascript:',
            b'vbscript:'
        ]
        
        for pattern in patterns:
            if re.search(pattern, data, re.IGNORECASE):
                suspicious.append(pattern.decode())
        
        return suspicious
    
    def extract_potential_code(self, data):
        # Look for base64 encoded data
        base64_pattern = b'[A-Za-z0-9+/]{20,}={0,2}'
        base64_matches = re.findall(base64_pattern, data)
        
        # Look for hex encoded data
        hex_pattern = b'[0-9A-Fa-f]{32,}'
        hex_matches = re.findall(hex_pattern, data)
        
        result = "=== POTENTIAL HIDDEN CODE ===\n\n"
        
        if base64_matches:
            result += "BASE64 ENCODED DATA FOUND:\n"
            for match in base64_matches[:5]:  # Show first 5 matches
                result += f"{match.decode()}\n"
            result += "\n"
        
        if hex_matches:
            result += "HEX ENCODED DATA FOUND:\n"
            for match in hex_matches[:5]:  # Show first 5 matches
                result += f"{match.decode()}\n"
        
        return result if (base64_matches or hex_matches) else "No obvious encoded data found."
    
    def update_results(self, results):
        # Update code tab
        code_output = "=== EXTRACTED DATA ANALYSIS ===\n\n"
        code_output += "FILE INFORMATION:\n"
        for key, value in results['file_info'].items():
            code_output += f"{key.upper()}: {value}\n"
        
        code_output += "\nMETADATA:\n"
        for key, value in results['metadata'].items():
            code_output += f"{key}: {value}\n"
        
        code_output += "\nEXTRACTED STRINGS:\n"
        for string in results['hidden_strings'][:20]:  # Show first 20 strings
            code_output += f"{string}\n"
        
        code_output += f"\n{results['hex_data']}"
        
        self.code_text.insert(1.0, code_output)
        
        # Update analysis tab
        analysis_output = "=== SECURITY ANALYSIS RESULTS ===\n\n"
        
        if results['suspicious_patterns']:
            analysis_output += "🚨 SUSPICIOUS PATTERNS DETECTED:\n"
            for pattern in results['suspicious_patterns']:
                analysis_output += f"• {pattern}\n"
            analysis_output += "\n⚠️  POTENTIAL THREAT DETECTED!\n"
        else:
            analysis_output += "✅ No obvious malicious patterns detected.\n"
        
        analysis_output += f"\nFile Hash: {results['file_info'].get('md5_hash', 'N/A')}"
        analysis_output += f"\nFile Size: {results['file_info'].get('size', 'N/A')}"
        
        self.analysis_text.insert(1.0, analysis_output)
    
    def scan_for_virus(self):
        if not self.file_path.get():
            messagebox.showwarning("Warning", "Please select an image file first!")
            return
        
        self.progress.start()
        threading.Thread(target=self.perform_virus_scan, daemon=True).start()
    
    def perform_virus_scan(self):
        try:
            file_path = self.file_path.get()
            file_hash = self.calculate_file_hash(file_path)
            
            # Advanced heuristic analysis
            threat_level, details = self.heuristic_analysis(file_path)
            
            self.root.after(0, self.show_scan_results, threat_level, details, file_hash)
            
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", f"Scan failed: {str(e)}"))
        finally:
            self.root.after(0, self.progress.stop)
    
    def heuristic_analysis(self, file_path):
        try:
            with open(file_path, 'rb') as f:
                data = f.read()
            
            threat_score = 0
            details = []
            
            # Check file size anomalies
            file_size = len(data)
            if file_size > 10 * 1024 * 1024:  # Larger than 10MB
                threat_score += 1
                details.append("Large file size - potential data hiding")
            
            # Check for embedded scripts
            script_patterns = [
                b'<script>', b'<?php', b'<%@', b'<%=', 
                b'python', b'import', b'require', b'include'
            ]
            for pattern in script_patterns:
                if pattern in data.lower():
                    threat_score += 2
                    details.append(f"Embedded script pattern found: {pattern}")
            
            # Check for encoded data
            if b'base64' in data.lower():
                threat_score += 1
                details.append("Base64 encoding detected")
            
            # Check for executable patterns
            if b'MZ' in data[:2]:  # Windows executable
                threat_score += 3
                details.append("Executable file signature detected")
            
            # Determine threat level
            if threat_score >= 3:
                return "HIGH", details
            elif threat_score >= 1:
                return "MEDIUM", details
            else:
                return "LOW", details
                
        except Exception as e:
            return "UNKNOWN", [f"Analysis error: {str(e)}"]
    
    def show_scan_results(self, threat_level, details, file_hash):
        color_map = {
            "HIGH": "#ff0000",
            "MEDIUM": "#ff9900", 
            "LOW": "#00ff00",
            "UNKNOWN": "#ffff00"
        }
        
        result_window = tk.Toplevel(self.root)
        result_window.title("Virus Scan Results")
        result_window.geometry("600x400")
        result_window.configure(bg='#1a1a1a')
        
        # Threat level display
        threat_frame = tk.Frame(result_window, bg='#1a1a1a')
        threat_frame.pack(fill='x', padx=20, pady=20)
        
        tk.Label(
            threat_frame,
            text="SCAN RESULTS:",
            font=('Arial', 16, 'bold'),
            fg='#ffffff',
            bg='#1a1a1a'
        ).pack()
        
        tk.Label(
            threat_frame,
            text=f"THREAT LEVEL: {threat_level}",
            font=('Arial', 20, 'bold'),
            fg=color_map.get(threat_level, '#ffffff'),
            bg='#1a1a1a'
        ).pack(pady=10)
        
        # File hash
        tk.Label(
            threat_frame,
            text=f"File Hash: {file_hash}",
            font=('Courier', 10),
            fg='#66ccff',
            bg='#1a1a1a'
        ).pack()
        
        # Details
        details_frame = tk.Frame(result_window, bg='#1a1a1a')
        details_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        details_text = scrolledtext.ScrolledText(
            details_frame,
            bg='#000000',
            fg='#ffffff',
            font=('Arial', 10),
            wrap=tk.WORD
        )
        details_text.pack(fill='both', expand=True)
        
        if details:
            details_text.insert(1.0, "DETAILED ANALYSIS:\n\n")
            for detail in details:
                details_text.insert(tk.END, f"• {detail}\n")
        else:
            details_text.insert(1.0, "No specific threats detected.")
        
        details_text.config(state=tk.DISABLED)
    
    def clear_all(self):
        self.file_path.delete(0, tk.END)
        self.code_text.delete(1.0, tk.END)
        self.analysis_text.delete(1.0, tk.END)
        self.image_label.configure(image='', text="No Image Selected")
        self.progress.stop()

def main():
    root = tk.Tk()
    app = ChowdhuryVaiImageAnalyzer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
