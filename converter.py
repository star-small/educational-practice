import json

def convert_to_yolo(x, y, width, height, img_width, img_height):
    x_center = (x + width / 2) / img_width
    y_center = (y + height / 2) / img_height
    width_norm = width / img_width
    height_norm = height / img_height
    return x_center, y_center, width_norm, height_norm

label_to_class_id = {
    "Lamp": 0,
    "Pole": 1,
}

def process_annotations(json_file, output_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    with open(output_file, 'w') as f_out:
        for item in data:
            if item['annotations']:  
                annotation = item['annotations'][0]['result']
                if annotation:  # Check if result list is not empty
                    value = annotation[0]['value']
                    x, y, width, height = value['x'], value['y'], value['width'], value['height']
                    rectanglelabel = value['rectanglelabels'][0]  # Convert list to string
                    image_path = item['data']['image']

                    img_width = 1280  
                    img_height = 720  

                    x_center, y_center, width_norm, height_norm = convert_to_yolo(x, y, width, height, img_width, img_height)
                    class_id = label_to_class_id.get(rectanglelabel, -1)                      if class_id != -1:
                        f_out.write(f"{class_id} {x_center} {y_center} {width_norm} {height_norm}\n")

json_file = 'file.json'  
output_file = 'output.txt' 
process_annotations(json_file, output_file)

print("YOLO formatted data has been written to", output_file)

