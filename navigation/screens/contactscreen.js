import * as React from 'react';
import { View, Text } from 'react-native';
import { useState,useEffect } from 'react';
import axios from 'axios'
export default function contactScreen({ navigation }) {
    const[data,setData]=useState([])

    const fetchdata=()=>{
      axios.get('http://127.0.0.1:8000/manage/employee').
      then((response)=>
       setData(response.data)
      )
     }
     const deletedata=(id)=>{

        axios.delete(`http://127.0.0.1:8000/manage/empdel/${id}`).then(
          fetchdata()
        )
       }
        
     useEffect(()=>{
     fetchdata()
     },[])
     return(
    
        <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
            {
            data.map((d)=>{
            return(
        
      <Text onPress={() => navigation.navigate('Home')}
      style={{ fontSize: 26, fontWeight: 'bold' }}>
            First name:{d.fname}<br></br> salary:{d.salary}<br></br>
      
      
      <button onClick={()=>deletedata(d.id)} >delete</button>
                
            </Text>)
           })}
        </View>
    
    );}
