//
//  ContentView.swift
//  sauMenu
//
//  Created by Andrew Hansbury on 12/8/21.
//

import SwiftUI
import Foundation

struct Food: Identifiable, Decodable {
    var Day: String
    var Breakfast: String
    var Lunch: String
    var Dinner: String
    var id: String{Day}
}


class Network: ObservableObject {
    @Published var d: [Food] = []
    
    func dataHandler() {
        
        let url = URL(string: "https://menujson.000webhostapp.com/")!
        
        print("")
        var request = URLRequest(url: url)
        request.httpMethod = "GET"
        
        let task = URLSession.shared.dataTask(with: url) { (data, response, error) in
            if let error = error {
                print(error)
                return
            }
            
            guard let response = response as? HTTPURLResponse else {return}
            
            print(response.statusCode)
            
            if response.statusCode == 200{
                guard let data = data else {return}
                DispatchQueue.main.async {
                    do {
                        let decode = try JSONDecoder().decode([Food].self, from: data)
                        self.d = decode
                    } catch let error {
                        print("Ouchy", error)
                    }
                }
            }
        }
        print(d)
        task.resume()
    }
}



var d = ""

struct ContentView: View {
    @EnvironmentObject var network: Network
    
    
    @State var menu: [String] = ["hi", "hi"]
    
    var body: some View {
        List{
            ForEach(network.d) { item in
                Text(item.Breakfast)
                Text(item.Lunch)
                Text(item.Dinner)
            }
        }
        .onAppear(perform: {
            network.dataHandler()
        })
    }
}


struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
            .environmentObject(Network())
    }
}
