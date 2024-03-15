import idaapi
import idautils
import idc
import re

def extract_names_and_rva_base(file_path):
    # Regular expression pattern to match lines with the desired format
    pattern = r"\s(\d+):([a-fA-F0-9]+)\s+(\S+)\s+([a-fA-F0-9]+)\s+(.+)"
    results = []

    # Open the file and read line by line
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            match = re.search(pattern, line)
            if match:
                # Extract name and Rva+Base
                section_number, offset, name, rva_base, _ = match.groups()
                # Convert Rva+Base to an integer in hexadecimal
                results.append((name, int(rva_base, 16)))  
    return results

def rename_symbols_from_map():
    # Use idaapi.ask_file to show a file selection dialog for choosing a .map file
    map_file_path = idaapi.ask_file(0, "*.map", "Please select a .map file to parse")
    if map_file_path:
        extracted_data = extract_names_and_rva_base(map_file_path)
        for name, rva_base in extracted_data:
            # Use idaapi.set_name to rename the corresponding address, ensuring the address is valid
            if idc.get_segm_name(rva_base) is not None:
                idaapi.set_name(rva_base, name, idaapi.SN_NOWARN)
        print(f"Processed {len(extracted_data)} symbols.")
    else:
        print("No .map file selected.")

rename_symbols_from_map()
