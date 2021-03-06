/***************************************************************************
 *  drilling_machine_plugin.cpp - Drilling machine plugin
 *
 *  Created: Mon Nov 12 09:14:11 2014
 *  Copyright  2014 Frederik Hegger
 ****************************************************************************/

/*  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU Library General Public License for more details.
 *
 *  Read the full text in the LICENSE.GPL file in the doc directory.
 */

#include <core/plugin.h>

#include "drilling_machine_thread.h"

using namespace fawkes;

/** Plugin to interface with drilling machine device
 * @author Frederik Hegger
 */
class DrillingMachinePlugin: public fawkes::Plugin
{
    public:
        /** Constructor.
         * @param config Fawkes configuration
         */
        DrillingMachinePlugin(Configuration *config) :
                Plugin(config)
        {
            thread_list.push_back(new DrillingMachineThread());
        }
};

PLUGIN_DESCRIPTION("Plugin to communicate with the drilling machine")
EXPORT_PLUGIN(DrillingMachinePlugin)
