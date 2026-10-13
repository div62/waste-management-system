from backend.vendor_manager import view_vendors
vendors = view_vendors()
if vendors:
    for vendor in vendors:
        print(vendor)
else:
    print("No vendors found.")
from backend.vendor_manager import search_vendors
vendors = search_vendors(
    "Amritsar",
    "Plastic",
    "New Amritsar"
)
if vendors:
    for vendor in vendors:
        print(vendor)
else:
    print("No matching vendors found.")    
from backend.vendor_manager import update_vendor, view_vendors
update_vendor(
    1,
    "Bca Updated",
    "Amritsar",
    "New Amritsar",
    "Plastic",
    "9876543210"
)
vendors = view_vendors()
for vendor in vendors:
    print(vendor)
from backend.vendor_manager import delete_vendor, view_vendors
deleted = delete_vendor(1)
if deleted > 0:
    print("Vendor deleted successfully!")
else:
    print("Vendor not found!")
print("\nRemaining vendors:")
for vendor in view_vendors():
    print(vendor)    