#include <sstream>
#include <map>
#include <boost/property_tree/ptree.hpp>
#include <boost/property_tree/json_parser.hpp>

// Using boost - remember to install if you haven't already!
using boost::property_tree::ptree;
using boost::property_tree::read_json;
using boost::property_tree::write_json;

int main() {
  // Read json
  std::ifstream ifs("v3.json");
  ptree pt;
  read_json(ifs, pt);
  ifs.close();

  // Pretend to do something here
  ptree lang;
  lang.put("", "c++");
  pt.get_child("languages").push_back(std::make_pair("", lang));

  // Write json
  std::ofstream ofs("v4.json");
  write_json(ofs, pt, false);
  ofs.close();

  return 1;
}
