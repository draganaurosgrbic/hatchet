#!/usr/bin/env python
#
# Copyright 2017-2023 Lawrence Livermore National Security, LLC and other
# Hatchet Project Developers. See the top-level LICENSE file for details.
#
# SPDX-License-Identifier: MIT

import hatchet as ht


if __name__ == "__main__":
    # Path to caliper cali file.
    cali_file = "../../../hatchet/tests/data/caliper-example-cali/example-profile.cali"

    gf = ht.GraphFrame.from_caliperreader(cali_file)

    # Printout the DataFrame component of the GraphFrame.
    print(gf.dataframe)

    # Printout the graph component of the GraphFrame with the specified metric.
    print(gf.tree(metric_column="avg#inclusive#sum#time.duration"))
