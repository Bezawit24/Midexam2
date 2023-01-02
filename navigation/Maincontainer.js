import * as React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import Ionicons from 'react-native-vector-icons/Ionicons';

// Screens
import HomeScreen from './screens/homescreen'
import contactScreen from './screens/contactscreen'
import aboutScreen from './screens/Aboutscreen'

//Screen names
const homeName = "Students";
const AboutName = "Employee";
const contactName = "Teachers";

const Tab = createBottomTabNavigator();

function MainContainer() {
  return (
    <NavigationContainer>
      <Tab.Navigator
        initialRouteName={homeName}
        screenOptions={({ route }) => ({
          tabBarIcon: ({ focused, color, size }) => {
            let iconName;
            let rn = route.name;

            if (rn === homeName) {
              iconName = focused ? 'home' : 'home-outline';

            } else if (rn === AboutName) {
              iconName = focused ?  'information' : 'information-circle-sharp';

            } else if (rn === contactName) {
              iconName = focused ? 'chatbubbles-sharp' : 'chatbubbles-sharp';
            }
 
            // You can return any component that you like here!
            return <Ionicons name={iconName} size={size} color={color} />;
          },
        })}
        tabBarOptions={{
          activeTintColor: 'tomato',
          inactiveTintColor: 'grey',
          labelStyle: { paddingBottom: 10, fontSize: 10 },
          style: { padding: 10, height: 70}
        }}>

        <Tab.Screen name={homeName} component={HomeScreen} />
        <Tab.Screen name={contactName} component={contactScreen} />
        <Tab.Screen name={AboutName} component={aboutScreen} />

      </Tab.Navigator>
    </NavigationContainer>
  );
}

export default MainContainer;
