//
//  sauMenuApp.swift
//  sauMenu
//
//  Created by Andrew Hansbury on 12/8/21.
//

import SwiftUI

@main
struct sauMenuApp: App {
    var network = Network()
    var body: some Scene {
        WindowGroup {
            ContentView()
                .environmentObject(Network())
        }
    }
}
