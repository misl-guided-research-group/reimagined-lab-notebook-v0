import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;

public class InventorySystemDesign{

    Member member; 
    


    public static void main(String[] args){

        // inventory 
        List<Component> inventoryArray = new ArrayList<Component>();


        Member member = new Member("Hawa", "Drammeh");

        // pretty sure we can just use an alhambra class
        Component m1 = new Component(member, "MgCl", "10X", false);
        Component m2 = new Component(member, "NaCi", "1M", true);

        inventoryArray.add(m1);

        inventoryArray.add(m2);

        for(Component c : inventoryArray){
            System.out.println(c.componentName);
            System.out.println(c.concentration);
            System.out.println(c.componentID);
            System.out.println(c.currTime);

            System.out.println("------------------------------------");
        }

    }

    static class Member{
        String firstName; 
        String lastName;
        
        public Member(String firstName, String lastName){
            this.firstName = firstName;
            this.lastName = lastName;
        }
    }

    static class Component {
        Member creator; 
        String componentName;
        String concentration; //number or string
        String componentID;
        // should we potentially have a count of how many vials of saif unique component?
        boolean isBuffer;
        LocalDateTime currTime;


        public Component(Member creator, String componentName, String concentration, boolean isBuffer){

            DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy/MM/dd HH:mm:ss");
            currTime = LocalDateTime.now();

            this.creator = creator;
            this.componentName = componentName;
            this.concentration = concentration;
            this.componentID = this.componentName + "_" + this.concentration;

        }
    }

}

/*
 * def __init__(self):
        self.inventory_dict = {}
        
    def add_component(self, component):
        if component.component_id not in self.inventory_dict:
            self.inventory_dict[component.component_id] = {'component': component, 'quantity': 1}
        else:
            self.inventory_dict[component.component_id]['quantity'] += 1
            
    def remove_component(self, component_id):
        if component_id in self.inventory_dict:
            if self.inventory_dict[component_id]['quantity'] > 1:
                self.inventory_dict[component_id]['quantity'] -= 1
            else:
                self.inventory_dict.pop(component_id)
                
    def get_inventory(self):
        for component_id, component_data in self.inventory_dict.items():
            component = component_data['component']
            quantity = component_data['quantity']
            print(f"  {component.concentration} of component: {component.component_name} added to inventory")
            print(f"Component ID: {component.component_id}")
            print(f"Created by: {component.creator.first_name} {component.creator.last_name}")
            print(f"Quantity: {quantity}")
            print(f"Date added: {component.curr_time}")
            print("------------------------------------")
 */