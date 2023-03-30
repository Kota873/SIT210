/*
  Copyright (C) 2014 Alik <aliktab@gmail.com> All rights reserved.

  This library is free software; you can redistribute it and/or
  modify it under the terms of the GNU Lesser General Public
  License as published by the Free Software Foundation; either
  version 2.1 of the License, or (at your option) any later version.

  This library is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
  Lesser General Public License for more details.

  You should have received a copy of the GNU Lesser General Public
  License along with this library; if not, write to the Free Software
  Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
*/

#include "BH1750.h"
BH1750 sensor(0x23, Wire);

#define SUN_LIGHT 10000
void setup()
{
  sensor.begin();

  sensor.set_sensor_mode(BH1750::forced_mode_high_res2);

  Serial.begin();
}

void loop()
{
  sensor.make_forced_measurement();

  Serial.println(String::format("%f", sensor.get_light_level()));
  
  if (sensor.get_light_level() >= SUN_LIGHT){
            // Particle.publish("sun", "hit");
            Particle.publish("sun", "hit",PRIVATE);
            //sum = sum + sensor.get_light_level();
            //sun_light = sun_light + sensor.get_light_level();
            
            }
  else if(sensor.get_light_level() < SUN_LIGHT){
            // Particle.publish("sum", "not hit");
            Particle.publish("sun", "not hit",PRIVATE);
            
            }
        
  delay(60000);// delay 1 minuts
  delay(300000); // delay 5 minuts
  
  

}
