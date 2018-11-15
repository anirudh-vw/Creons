#!/usr/bin/python
import os
import shutil
import argparse
import progressbar
import inspect
from time import sleep

parser=argparse.ArgumentParser()
parser.add_argument('-proj', required = True)
args=parser.parse_args()

proj_name=args.proj 
print "Project name: ", proj_name

proj_pkg=args.proj + '_pkg'
proj_xactn=args.proj + '_xactn'
proj_if=args.proj + '_if'
proj_if_0=args.proj + '_if_0'
proj_sva_if=args.proj + '_sva_if'
proj_sva_bind=args.proj + '_sva_bind'
proj_sequencer=args.proj + '_sequencer'
proj_driver=args.proj + '_driver'
proj_input_monitor=args.proj + '_input_monitor' 
proj_output_monitor=args.proj + '_output_monitor'
proj_agent=args.proj + '_agent'
proj_env=args.proj + '_env'
proj_scoreboard=args.proj + '_scoreboard'
proj_fcover=args.proj + '_fcover'
proj_include=args.proj + '_include'
proj_base_test=args.proj + '_base_test'
proj_rand_seq=args.proj + '_rand_seq'
proj_seq_lib=args.proj + '_seq_lib'
proj_tb_dut_top=args.proj + '_tb_dut_top'
proj_rand_test=args.proj + '_rand_test'

def createProgressBar():
  bar = progressbar.ProgressBar(maxval=40, \
  widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
  bar.start()
  for i in xrange(40):
    bar.update(i+1)
    sleep(0.1)
  bar.finish()


def createTransactionheader():
	print "Creating transaction header component..."
	op_f = open('tb_src/'+proj_xactn+'.svh', 'w')
	print >> op_f, "import "+proj_pkg+"::*;\n"
	print >> op_f, "class "+proj_xactn+" extends uvm_sequence_item;\n "
        print >> op_f, "  `uvm_object_utils_begin("+proj_xactn+")"
        print >> op_f, "  `uvm_object_utils_end\n"
        print >> op_f, "  extern function new(string name=\""+proj_xactn+"\");"
        print >> op_f, "endclass : "+proj_xactn+"\n"
        vw_show_progress()

def createTransaction():
	print "Creating transaction  component..."
	op_f = open('tb_src/'+proj_xactn+'.sv', 'w')
        print >> op_f, "function "+proj_xactn+":: new(string name=\""+proj_xactn+"\");"
        print >> op_f, "  super.new(name);"
        print >> op_f, "endfunction : new\n"
        vw_show_progress()


def createSequencerheader() :
	 print "Creating sequencer header component..."
         vw_show_progress()
	 op_f = open ('tb_src/'+proj_sequencer+'.svh', 'w')
         print >> op_f, "class "+proj_sequencer+" extends uvm_sequencer #("+proj_xactn+");\n"
         print >> op_f, "  `uvm_component_utils("+proj_sequencer+")\n" 
	 print >> op_f, "  extern function new(string name, uvm_component parent);"
         print >> op_f, "endclass : "+proj_sequencer+""
         vw_show_progress()

def createSequencer() :
	 print "Creating sequencer component..."
	 op_f = open ('tb_src/'+proj_sequencer+'.sv', 'w') 
	 print >> op_f, "function "+proj_sequencer+"::new(string name, uvm_component parent);"
         print >> op_f, "  super.new(name,parent);"
         print >> op_f, "endfunction : new\n"
         vw_show_progress()
 

def createInmonitorheader() :
	print "Creating input monitor header component..."
	op_f = open('tb_src/'+proj_input_monitor+'.svh', 'w')
        print >> op_f, "class "+proj_input_monitor+" extends uvm_monitor;\n"
        print >> op_f, "  virtual "+proj_if_0+" vif;\n"
        print >> op_f, "  "+proj_xactn+" x0;\n"
        print >> op_f, "  //TLM port for scoreboard communication" 
        print >> op_f, "  // (implement scoreboard write method if needed)\n"
        print >> op_f, "  uvm_analysis_port #("+proj_xactn+") m_in_aport;\n"
        print >> op_f, "  `uvm_component_utils_begin("+proj_input_monitor+")"
        print >> op_f, "    `uvm_field_object(x0, UVM_ALL_ON)"
        print >> op_f, "  `uvm_component_utils_end\n"
        print >> op_f, "  extern function new(string name, uvm_component parent);"
        print >> op_f, "  extern virtual task run_phase(uvm_phase phase);"
        print >> op_f, "  extern virtual task collect_data();\n"
        print >> op_f, "endclass : "+proj_input_monitor+"\n"
        vw_show_progress()
        

def createInmonitor() :
	print "Creating input monitor component..."
	op_f = open('tb_src/'+proj_input_monitor+'.sv', 'w')
        print >> op_f,"function "+proj_input_monitor+"::new(string name, uvm_component parent);"
        print >> op_f,"  super.new(name,parent);"
        print >> op_f,"  m_in_aport = new(\"m_in_aport\", this);"
        print >> op_f,"endfunction : new\n"
        print >> op_f,"task "+proj_input_monitor+"::run_phase(uvm_phase phase);"
        print >> op_f,"  `uvm_info(get_name(),\"Run Phase is Running ..\\n\",UVM_HIGH)"
        print >> op_f,"  collect_data();"
        print >> op_f,"endtask : run_phase\n"
        print >> op_f,"task "+proj_input_monitor+"::collect_data();\n"
        print >> op_f,"  begin\n\n\n"
        print >> op_f,"  end"
        print >> op_f,"endtask : collect_data\n"
        vw_show_progress()



def createOutMonitorheader() :
	print "Creating output monitor header component..."
	op_f = open ('tb_src/'+proj_output_monitor+'.svh', 'w') 
	print >> op_f,"class "+proj_output_monitor+" extends uvm_monitor;\n"
        print >> op_f,"  virtual "+proj_if_0+" vif;\n"
        print >> op_f,"  "+proj_xactn+" x0;\n"
        print >> op_f,"  //TLM port for scoreboard communication" 
        print >> op_f,"  // (implement scoreboard write method if needed)\n"
        print >> op_f,"  uvm_analysis_port #("+proj_xactn+") m_out_aport;\n"
        print >> op_f,"  `uvm_component_utils_begin("+proj_output_monitor+")"
        print >> op_f,"    `uvm_field_object(x0, UVM_ALL_ON)"
        print >> op_f,"  `uvm_component_utils_end\n"
        print >> op_f,"  extern function new(string name, uvm_component parent);"
        print >> op_f,"  extern virtual task run_phase(uvm_phase phase);"
        print >> op_f,"  extern virtual task collect_data();\n"
        print >> op_f, "endclass : "+proj_output_monitor+"\n"
        vw_show_progress()
       

def createOutMonitor() :
	print "Creating output monitor component..."
	op_f = open ('tb_src/'+proj_output_monitor+'.sv', 'w') 
        print >> op_f,"function "+proj_output_monitor+"::new(string name, uvm_component parent);"
        print >> op_f,"  super.new(name,parent);"
        print >> op_f,"  m_out_aport = new(\"m_out_aport\", this);"
        print >> op_f,"endfunction : new\n"
        print >> op_f,"task "+proj_output_monitor+"::run_phase(uvm_phase phase);"
        print >> op_f,"  `uvm_info(get_name(),\"Run Phase is Running ..\\n\",UVM_HIGH)"
        print >> op_f,"  collect_data();"
        print >> op_f,"endtask : run_phase\n"
        print >> op_f,"task "+proj_output_monitor+"::collect_data();"
        print >> op_f,"  begin\n\n"
        print >> op_f,"  end\n"
        print >> op_f,"endtask : collect_data\n"
        vw_show_progress()


def createFuncCovheader () :
	print "Creating functional coverage header component..."
        op_f = open ('tb_src/'+proj_fcover+'.svh','w')
	print >> op_f,"class "+proj_fcover+" extends uvm_subscriber #("+proj_xactn+");\n"
	print >> op_f,"  "+proj_xactn+" tr;\n"
	print >> op_f,"  `uvm_component_utils_begin("+proj_fcover+")"
	print >> op_f,"    `uvm_field_object(tr, UVM_ALL_ON)"
	print >> op_f,"  `uvm_component_utils_end\n"
	print >> op_f,"   uvm_analysis_imp #("+proj_xactn+","+proj_fcover+") cover_port;\n"
	print >> op_f,"  covergroup coverg;\n\n\n"
	print >> op_f,"  endgroup : coverg\n"
	print >> op_f,"  extern function new (string name, uvm_component parent);"
	print >> op_f,"  extern virtual task run_phase(uvm_phase phase);"
	print >> op_f,"  extern virtual function void write("+proj_xactn+" t);"
        print >> op_f,"  extern virtual function void report_phase (uvm_phase phase);\n"
	print >> op_f,"endclass : "+proj_fcover+"\n"
        vw_show_progress()

def createFuncCov () :
	print "Creating functional coverage component..."
        op_f = open ('tb_src/'+proj_fcover+'.sv','w')
	print >> op_f,"function "+proj_fcover+":: new (string name, uvm_component parent);"
	print >> op_f,"  super.new(name,parent);"
	print >> op_f,"  cover_port = new(\"cover_port\",this);"
	print >> op_f,"  this.coverg = new();"
	print >> op_f,"endfunction : new\n"
	print >> op_f,"function void "+proj_fcover+"::write("+proj_xactn+" t);"
	print >> op_f,"  this.tr = t;"
	print >> op_f,"  this.coverg.sample();"
	print >> op_f,"endfunction : write\n"
	print >> op_f,"task "+proj_fcover+"::run_phase(uvm_phase phase);"
	print >> op_f,"  `uvm_info(get_name(),$sformatf(\"Run Phase is running ..\\n\"),UVM_MEDIUM)"
	print >> op_f,"endtask : run_phase\n"
	print >> op_f,"function void "+proj_fcover+"::report_phase (uvm_phase phase);"
	print >> op_f,"  `uvm_info (get_name(), $sformatf ( \"The Functional Coverage: %f\", this.coverg.get_coverage()), UVM_NONE)"
	print >> op_f,"endfunction : report_phase\n"
        vw_show_progress()



def createScoreboardheader() :
	 print "Creating scoreboard header component..."
	 op_f = open('tb_src/'+proj_scoreboard+'.svh','w')
	 print >> op_f,"class "+proj_scoreboard+" extends uvm_scoreboard;\n"
	 print >> op_f,"  "+proj_xactn+" trans;\n"
	 print >> op_f,"  `uvm_component_utils_begin("+proj_scoreboard+")"
	 print >> op_f,"    `uvm_field_object(trans, UVM_ALL_ON)"
	 print >> op_f,"  `uvm_component_utils_end\n"
	 print >> op_f,"  uvm_tlm_analysis_fifo #("+proj_xactn+") m_in_afifo;"
	 print >> op_f,"  uvm_tlm_analysis_fifo #("+proj_xactn+") m_out_afifo;\n"
	 print >> op_f,"  extern function new(string name, uvm_component parent);"
	 print >> op_f,"  extern virtual task run_phase(uvm_phase phase);\n"
	 print >> op_f,"endclass : "+proj_scoreboard+"\n"
         vw_show_progress()

def createScoreboard() :
	 print "Creating scoreboard component..."
	 op_f = open('tb_src/'+proj_scoreboard+'.sv','w')	 
	 print >> op_f,"function "+proj_scoreboard+"::new(string name, uvm_component parent);"
	 print >> op_f,"  super.new(name,parent);"
	 print >> op_f,"  m_in_afifo = new(\"m_in_afifo\",this);"
	 print >> op_f,"  m_out_afifo = new(\"m_out_afifo\",this);"
	 print >> op_f,"endfunction : new\n"
	 print >> op_f,"task "+proj_scoreboard+"::run_phase(uvm_phase phase);\n"
	 print >> op_f,"  `uvm_info(get_name(),\"Run phase is Running ..\\n\",UVM_HIGH)"
	 print >> op_f,"  begin\n\n"
	 print >> op_f,"  end"
	 print >> op_f,"endtask : run_phase\n"
         vw_show_progress()


def createDriverheader() :
	print "Creating driver header component...\n"
	op_f = open('tb_src/'+proj_driver+'.svh', 'w')
	print >> op_f,"class "+proj_driver+" extends uvm_driver #("+proj_xactn+");\n"
	print >> op_f,"  virtual "+proj_if_0+" vif;\n"
	print >> op_f,"  "+proj_xactn+" item;\n"
	print >> op_f,"  extern function new(string name, uvm_component parent);"	
	print >> op_f,"  `uvm_component_utils_begin("+proj_driver+")"
	print >> op_f,"    `uvm_field_object(item, UVM_ALL_ON)"
	print >> op_f,"  `uvm_component_utils_end\n"
	print >> op_f,"  extern virtual task reset_phase(uvm_phase phase);"
	print >> op_f,"  extern virtual task main_phase(uvm_phase phase);\n"
	print >> op_f,"endclass : "+proj_driver+"\n"
        vw_show_progress()

def createDriver() :
	print "Creating driver component...\n"
	op_f = open('tb_src/'+proj_driver+'.sv', 'w')
	print >> op_f,"function "+proj_driver+"::new(string name, uvm_component parent);"
	print >> op_f,"  super.new(name,parent);"
	print >> op_f,"endfunction : new\n"
	print >> op_f,"task "+proj_driver+"::reset_phase(uvm_phase phase);"
	print >> op_f,"  `uvm_info(get_name(),\"Reset Phase is Running ....\\n\",UVM_HIGH)"
	print >> op_f,"  begin\n"
	print >> op_f,"    phase.raise_objection(this);\n\n"
	print >> op_f,"    phase.drop_objection(this);"
	print >> op_f,"  end"
	print >> op_f,"endtask : reset_phase\n"
	print >> op_f,"task "+proj_driver+"::main_phase(uvm_phase phase);\n"
	print >> op_f,"  `uvm_info(get_name(),\"Main Phase is Running ....\\n\",UVM_HIGH)"
	print >> op_f,"  forever"
	print >> op_f,"    begin"
	print >> op_f,"      seq_item_port.get_next_item(this.item);"
	print >> op_f,"      phase.raise_objection(this);\n\n"
	print >> op_f,"      seq_item_port.item_done();"
	print >> op_f,"      phase.drop_objection(this);"
	print >> op_f,"    end"
	print >> op_f,"endtask : main_phase\n"
        vw_show_progress()


def cretaeAgentheader() :
	print "Creating agent header component..."
	op_f = open('tb_src/'+proj_agent+'.svh', 'w')
	print >> op_f,"class "+proj_agent+" extends uvm_agent;\n"
	print >> op_f,"  uvm_active_passive_enum is_active;\n"
	print >> op_f,"  "+proj_sequencer+" sequencer_0;\n"
	print >> op_f,"  "+proj_driver+" driver_0;\n"
	print >> op_f,"  "+proj_input_monitor+" in_monitor_0;\n"
	print >> op_f,"  "+proj_output_monitor+" out_monitor_0;\n"
	print >> op_f,"  "+proj_scoreboard+" scoreboard_0;\n"
	print >> op_f,"  "+proj_fcover+" fcover_0;\n\n"
	print >> op_f,"  virtual "+proj_if_0+" vif;\n\n"
	print >> op_f,"  `uvm_component_utils_begin ("+proj_agent+")\n"
	print >> op_f,"    `uvm_field_enum(uvm_active_passive_enum, is_active, UVM_ALL_ON)\n"
	print >> op_f,"  `uvm_component_utils_end\n\n"
	print >> op_f,"  extern function new(string name, uvm_component parent);\n"	
	print >> op_f,"  extern virtual function void build_phase(uvm_phase phase);\n"
	print >> op_f,"  extern virtual function void connect_phase(uvm_phase phase);\n"
	print >> op_f,"endclass : "+proj_agent+"\n"
        vw_show_progress()

def cretaeAgent() :
	print "Creating agent component..."
	op_f = open('tb_src/'+proj_agent+'.sv', 'w')
	print >> op_f,"function "+proj_agent+"::new(string name, uvm_component parent);\n"
	print >> op_f,"  super.new(name,parent);\n"
	print >> op_f,"endfunction : new\n"
	print >> op_f,"function void "+proj_agent+"::build_phase(uvm_phase phase);\n"
	print >> op_f,"  super.build_phase(phase);\n"
	print >> op_f,"    if (!uvm_config_db#(uvm_active_passive_enum)::get(this,"
        print >> op_f,"      				      \"\","
    	print >> op_f,"                	              \"is_active\","
    	print >> op_f," 				      is_active)) begin : def_val_for_is_active\n"
        print >> op_f,"        `uvm_warning(get_name(),$sformatf(\"No override for is_active: Using default is_active as:%s\","
        print >> op_f,"                                            this.is_active.name));"
        print >> op_f,"      end : def_val_for_is_active\n"
        print >> op_f,"  `uvm_info(get_name(),$sformatf(\"is_active is set to %s\",this.is_active.name),UVM_MEDIUM);\n"
	print >> op_f,"  in_monitor_0="+proj_input_monitor+"::type_id::create(\"input_monitor\",this);\n"
	print >> op_f,"  out_monitor_0="+proj_output_monitor+"::type_id::create(\"output_monitor\",this);\n"
	print >> op_f,"  scoreboard_0 ="+proj_scoreboard+"::type_id::create(\"scoreboard\",this);\n"
	print >> op_f,"  fcover_0 = "+proj_fcover+"::type_id::create(\"fcover\",this);\n"
	print >> op_f,"  if (is_active == UVM_ACTIVE)\n"
	print >> op_f,"    begin\n"
	print >> op_f,"      driver_0="+proj_driver+"::type_id::create(\"driver\",this);\n"
	print >> op_f,"      sequencer_0="+proj_sequencer+"::type_id::create(\"sequencer\",this);\n"
	print >> op_f,"    end\n"
	print >> op_f,"endfunction : build_phase\n"
	print >> op_f,"function void "+proj_agent+"::connect_phase(uvm_phase phase);\n"
	print >> op_f,"  if(!uvm_config_db#(virtual "+proj_if_0+")::get(this,"
        print >> op_f,"		                    \"\","
        print >> op_f," 			            \"vif\","
        print >> op_f,"	            	            vif))\n"
        print >> op_f,"    begin:no_vif\n"
      	print >> op_f,"      `uvm_fatal(\"get_if_0\",\"no virtual interface available\");\n"
        print >> op_f,"    end:no_vif\n"
        print >> op_f,"  else\n"
        print >> op_f,"    begin:vi_assigned\n"
        print >> op_f,"      `uvm_info(\"get_if_0\",$sformatf(\"virtual interface connected\"),UVM_HIGH)\n"
        print >> op_f,"        this.vif = vif;\n"
        print >> op_f,"    end:vi_assigned\n\n"
	print >> op_f,"  in_monitor_0.vif = this.vif;\n"
	print >> op_f,"  out_monitor_0.vif = this.vif;\n"
	print >> op_f,"  if (is_active == UVM_ACTIVE)\n"
        print >> op_f,"    begin\n"
	print >> op_f,"      this.driver_0.seq_item_port.connect(sequencer_0.seq_item_export);\n"
	print >> op_f,"      this.driver_0.vif = this.vif;\n"
	print >> op_f,"    end\n\n"
	print >> op_f,"  this.in_monitor_0.m_in_aport.connect(this.scoreboard_0.m_in_afifo.analysis_export);\n"
	print >> op_f,"  this.out_monitor_0.m_out_aport.connect(this.scoreboard_0.m_out_afifo.analysis_export);\n"
	print >> op_f,"  this.out_monitor_0.m_out_aport.connect(this.fcover_0.cover_port);\n"
	print >> op_f,"endfunction : connect_phase\n"
        vw_show_progress()


def createEnvheader () :
	 print "Creating environment header component..."
	 op_f = open('tb_src/'+proj_env+'.svh', 'w')
	 print >> op_f,"class "+proj_env+" extends uvm_env;\n"
	 print >> op_f,"  "+proj_agent+" agent_0;\n"
	 print >> op_f,"  `uvm_component_utils("+proj_env+")\n"
	 print >> op_f,"  extern function new(string name, uvm_component parent);"
	 print >> op_f,"  extern virtual function void build_phase(uvm_phase phase);\n"
	 print >> op_f,"endclass : "+proj_env+"\n"

def createEnv () :
	 print "Creating environment component..."
	 op_f = open('tb_src/'+proj_env+'.sv', 'w')
	 print >> op_f,"function "+proj_env+"::new(string name, uvm_component parent);"
	 print >> op_f,"  super.new(name,parent);"
	 print >> op_f,"endfunction : new\n"
	 print >> op_f,"function void "+proj_env+"::build_phase(uvm_phase phase);"
	 print >> op_f,"  super.build_phase(phase);"
	 print >> op_f,"  agent_0 = "+proj_agent+"::type_id::create(.name(\"agent\"),"
	 print >> op_f,"                		   .parent(this));\n"
	 print >> op_f,"  uvm_config_db#(uvm_active_passive_enum)::set(.cntxt(this),"
 	 print >> op_f,"         			               .inst_name(\"*\"),"
         print >> op_f,"				               .field_name(\"is_active\"),"
	 print >> op_f,"				       	       .value(UVM_ACTIVE));"
	 print >> op_f,"endfunction : build_phase\n"
         vw_show_progress()


def createSva() :
  	print "Creating assertions interface component..."
  	op_f = open('tb_src/'+proj_sva_if+'.sv', 'w')
	print >> op_f,"interface "+proj_sva_if+" (input logic clk);\n"
  	print >> op_f,"  import "+proj_pkg+"::*;\n\n\n\n"
  	print >> op_f,"endinterface : "+proj_sva_if+"\n"
        vw_show_progress()

def createInterface() :
	print "Creating interface component..."
	op_f = open('tb_src/'+proj_if+'.sv', 'w')
	print >> op_f,"import "+proj_pkg+"::*;\n"
	print >> op_f,"interface "+proj_if_0+" (input logic clk);\n\n\n\n"
	print >> op_f,"endinterface : "+proj_if_0+"\n"
        vw_show_progress()
	
def createInclude () :
	print "Creating include header file...";
	op_f = open('tb_src/'+proj_include+'.svh', 'w')
	print >> op_f,"`include \""+proj_xactn+".svh\""
	print >> op_f,"`include \""+proj_xactn+".sv\""
	print >> op_f,"`include \""+proj_sequencer+".svh\""
	print >> op_f,"`include \""+proj_sequencer+".sv\""
	print >> op_f,"`include \""+proj_input_monitor+".svh\""
	print >> op_f,"`include \""+proj_input_monitor+".sv\""
	print >> op_f,"`include \""+proj_output_monitor+".svh\""
	print >> op_f,"`include \""+proj_output_monitor+".sv\""
	print >> op_f,"`include \""+proj_fcover+".svh\""
	print >> op_f,"`include \""+proj_fcover+".sv\""
	print >> op_f,"`include \""+proj_scoreboard+".svh\""
	print >> op_f,"`include \""+proj_scoreboard+".sv\""
	print >> op_f,"`include \""+proj_driver+".svh\""
	print >> op_f,"`include \""+proj_driver+".sv\""
	print >> op_f,"`include \""+proj_agent+".svh\""
	print >> op_f,"`include \""+proj_agent+".sv\""
	print >> op_f,"`include \""+proj_env+".svh\""
	print >> op_f,"`include \""+proj_env+".sv\""
	print >> op_f,"`include \""+proj_seq_lib+".sv\""
	print >> op_f,"`include \""+proj_base_test+".sv\""
        vw_show_progress()

def createPackage() :
	print "Creating package file...";
  	op_f = open('tb_src/'+proj_pkg+'.sv', 'w')
  	print >> op_f,"import uvm_pkg::*;\n"
  	print >> op_f,"`include \"uvm_macros.svh\"\n"
  	print >> op_f,"package "+proj_pkg+";\n\n\n"
  	print >> op_f,"endpackage: "+proj_pkg+"\n"
        vw_show_progress()
	

def createSvaBind() :
  	print "Creating assertions bind component..."
	op_f = open('tb_src/'+proj_sva_bind+'.sv', 'w')
	print >> op_f,"module "+proj_sva_bind+";\n"
	print >> op_f,"bind "+proj_if_0+" "+proj_sva_if+" sva_if_0(.*);\n"
	print >> op_f,"endmodule:"+proj_sva_bind+"\n"
        vw_show_progress()
        
	
# ------------------------------------------------------------------------ #
# Print run_dir directory
# ------------------------------------------------------------------------ #

def createUvmFlist () :
  	print "Creating flist file..."
  	op_f = open ('run_dir/flist','w')
	print >> op_f,"+incdir+../tb_src\n"
	print >> op_f,"+incdir+../seq_tests\n"
#	print >> op_f,"+incdir+../$dir_tree[2]\n"
	print >> op_f,"../tb_src/"+proj_pkg+".sv\n"
	print >> op_f,"../tb_src/"+proj_if+".sv\n"
	print >> op_f,"../tb_src/"+proj_sva_if+".sv\n"
	print >> op_f,"../tb_src/"+proj_sva_bind+".sv\n"
	print >> op_f,"../seq_tests/"+proj_tb_dut_top+".sv\n"
        vw_show_progress()
	
def createMakefile() :
  	print "Creating Makefile..."
  	op_f = open ('run_dir/Makefile','w')
	print >> op_f,"TOP=\n"
	print >> op_f,"TEST="+proj_rand_test+"\n\n"
	print >> op_f,"clean:"
	print >> op_f,"		rm -fr csrc* DVE* scsim* led* simv* ucli* inter*  work* *.cm *.daidir *.h vsim.wlf transcript INCA* *.log *.vstf *.key waves.shm dataset* *.cfg .athdl* *.txt* athdl_sv* *~* *.db* compile *.awc .simvision* cov_work"
	print >> op_f,"cvc1:clean"
	print >> op_f,"		VCS ?= vcs"
	print >> op_f,"		vcs -sverilog -debug_all -lca -ntb_opts uvm-1.1 -f flist -l go2uvm_comp.log -assert svaext -timescale=1ns/1ns"
	print >> op_f,"		./simv +UVM_TESTNAME=$(TEST) +UVM_VERBOSITY=UVM_HIGH -l go2uvm_run.log"
	print >> op_f,"cvc1_gui:"
	print >> op_f,"		vcs -sverilog -debug_all -lca -ntb_opts uvm-1.1 -f flist -l go2uvm_comp.log -assert svaext -timescale=1ns/1ns"
	print >> op_f,"		./simv +UVM_TESTNAME=$(TEST) +UVM_VERBOSITY=UVM_HIGH -l go2uvm_run.log -gui &"	
	print >> op_f,"cvc2:clean"
	print >> op_f,"		vlib work"
	print >> op_f,"		vlog  +acc -sv -mfcu -timescale 1ns/1ns  -f flist -l go2uvm_comp.log"
	print >> op_f,"		vsim -c +access +rw $(TOP) +UVM_TESTNAME=$(TEST) +UVM_VERBOSITY=UVM_HIGH  -novopt -do \"run -all;\"|tee go2uvm_comp_run.log"
	print >> op_f,"cvc2_gui:clean"
	print >> op_f,"		vlib work"
	print >> op_f,"		vlog  +acc -mfcu -sv -f flist  -l go2uvm_comp.log"
	print >> op_f,"		vsim +access +r $(TOP)  -novopt +UVM_TESTNAME=$(TEST) +UVM_VERBOSITY=UVM_HIGH  -do \"run -all;\" -l  go2uvm_run.log"
	print >> op_f,"cvc3:clean"
	print >> op_f,"		irun -access +rw -uvm -f flist +UVM_TESTNAME=$(TEST) +UVM_VERBOSITY=UVM_HIGH -l go2uvm_run.log" 
	print >> op_f,"cvc3_gui:clean"
	print >> op_f,"		irun -access +rw -uvm -f flist +UVM_TESTNAME=$(TEST) +UVM_VERBOSITY=UVM_HIGH -l go2uvm_run.log -gui &"
	print >> op_f,"cvc4:clean gen_rvra_do"
	print >> op_f,"		vsim -c -do go2uvm_rvra.do"
	print >> op_f,"cvc4_gui:clean gen_rvra_do"
	print >> op_f,"		vsim -do go2uvm_rvra.do"
	print >> op_f,"gen_rvra_do:"
	print >> op_f,"	 touch go2uvm_rvra.do "
	print >> op_f,"	 echo ""clear"" > go2uvm_rvra.do "
	print >> op_f,"	 echo ""alib work"" >> go2uvm_rvra.do " 
	print >> op_f,"	 echo ""adel -all"" >> go2uvm_rvra.do " 
	print >> op_f,"	 echo ""transcript file go2uvm_comp.log"" >> go2uvm_rvra.do "
	print >> op_f,"	 echo	""alog -dbg \$$UVMCOMP -msg 0 -error_limit 1 -f flist"" >> go2uvm_rvra.do "
	print >> op_f,"	 echo	""transcript file go2uvm_run.log"" >> go2uvm_rvra.do "
	print >> op_f,"	 echo	""asim +access +rw \$$UVMSIM $(TOP) +UVM_TESTNAME=$(TEST) +UVM_VERBOSITY=UVM_HIGH"" >> go2uvm_rvra.do "
	print >> op_f,"	 echo	""run -all "" >> go2uvm_rvra.do "
	print >> op_f,"	 echo	""exit "" >> go2uvm_rvra.do "
        vw_show_progress()
# ------------------------------------------------------------------------ #
# Print sequence tests							   #
# ------------------------------------------------------------------------ #
 
def createBaseTest() :
  	print "Creating Base test file ...";
  	op_f = open ('seq_tests/'+proj_base_test+'.sv','w')
  	print >> op_f,"class "+proj_base_test+" extends uvm_test;\n"
  	print >> op_f,"  "+proj_env+" env_0;\n"
	print >> op_f,"  `uvm_component_utils("+proj_base_test+")\n"
	print >> op_f,"  function new(string name, uvm_component parent);"
	print >> op_f,"    super.new(name,parent);"
	print >> op_f,"  endfunction : new\n"
	print >> op_f,"  extern virtual function void build_phase(uvm_phase phase);"
	print >> op_f,"  extern virtual function void connect_phase(uvm_phase phase);"
	print >> op_f,"  extern virtual task main_phase (uvm_phase phase);\n"
	print >> op_f,"endclass : "+proj_base_test+"\n"
	print >> op_f,"function void "+proj_base_test+"::build_phase(uvm_phase phase);"	
	print >> op_f,"  super.build_phase(phase);"
	print >> op_f,"  env_0 = "+proj_env+"::type_id::create(.name(\"env\"),"
	print >> op_f,"				.parent(this));"
	print >> op_f,"endfunction : build_phase\n"
	print >> op_f,"function void "+proj_base_test+"::connect_phase(uvm_phase phase);"
	print >> op_f,"  uvm_top.print_topology();"
	print >> op_f,"endfunction : connect_phase\n"
	print >> op_f,"task "+proj_base_test+"::main_phase(uvm_phase phase);"
	print >> op_f,"  phase.raise_objection(this);"
	print >> op_f,"  `uvm_info(\"Base Test\",\"Test is running...\",UVM_LOW)"
	print >> op_f,"  #1000"
	print >> op_f,"  //delay is simple end of test mechanism"
	print >> op_f,"  //use objections in sequences for better end of test detection"
	print >> op_f,"  `uvm_info(\"Base Test\",\"User activated end of simulation\",UVM_LOW)"
	print >> op_f,"  phase.drop_objection(this);"
	print >> op_f,"endtask : main_phase\n"
        vw_show_progress()
	

def createRandSeq() :
	print "Rand Sequence file....."
  	op_f = open ('seq_tests/'+proj_rand_seq+'.sv','w')
	print >> op_f,"class "+proj_rand_seq+" extends uvm_sequence #("+proj_xactn+");\n"
	print >> op_f,"  `uvm_object_utils("+proj_rand_seq+")\n"
	print >> op_f,"  function new(string name = \""+proj_rand_seq+"\");"
	print >> op_f,"    super.new(name);"
	print >> op_f,"  endfunction : new\n"
	print >> op_f,"  extern virtual task body();\n"
	print >> op_f,"endclass : "+proj_rand_seq+"\n"
	print >> op_f,"task "+proj_rand_seq+"::body();"
	print >> op_f,"  `uvm_info(get_name(),$sformatf(\":Sequence is Running ....\\n\"),UVM_LOW)\n"
	print >> op_f,"  `uvm_info(get_name(),$sformatf(\":Sequence is Complete ....\\n\"),UVM_LOW)\n"
	print >> op_f,"endtask : body\n"
        vw_show_progress()
	
def createRandTest() :
	print "Creating Rand Test file...";
  	op_f = open ('seq_tests/'+proj_rand_test+'.sv','w')
	print >> op_f,"class "+proj_rand_test+" extends "+proj_base_test+";\n"
	print >> op_f,"  `uvm_component_utils("+proj_rand_test+")\n"
	print >> op_f,"  "+proj_rand_seq+" rand_seq_0;\n"
	print >> op_f,"  extern virtual task main_phase(uvm_phase phase);\n"
	print >> op_f,"  function new(string name, uvm_component parent = null);"
	print >> op_f,"    super.new(name,parent);"
	print >> op_f,"  endfunction : new\n"
	print >> op_f,"endclass : "+proj_rand_test+" \n"
	print >> op_f,"task "+proj_rand_test+"::main_phase(uvm_phase phase);"
	print >> op_f,"  phase.raise_objection(this);"
	print >> op_f,"  `uvm_info(\"Rand Test\",\"Test is running...\",UVM_LOW)"
	print >> op_f,"  rand_seq_0 = "+proj_rand_seq+"::type_id::create(.name(\"rand_seq_0\"),"
	print >> op_f,"						.parent(this));"
	print >> op_f,"  this.rand_seq_0.start(env_0.agent_0.sequencer_0);"
	print >> op_f,"  #500;\n"
	print >> op_f,"  `uvm_info(\"Rand Test\",\"User activated end of simulation\",UVM_LOW)"
	print >> op_f,"  phase.drop_objection(this);\n"
	print >> op_f,"endtask : main_phase\n"
        vw_show_progress()
	

def createSeqLib () :
	print "Creating Sequence Library file...";
 	op_f = open ('seq_tests/'+proj_seq_lib+'.sv','w')
	print >> op_f,"`include \""+proj_rand_seq+".sv\"\n"
        vw_show_progress()
	

def createTbDutTop () :
  	print "Creating top file..."
  	op_f = open ('seq_tests/'+proj_tb_dut_top+'.sv','w')
  	print >> op_f,"module tb_top();\n"
  	print >> op_f,"`include \""+proj_include+".svh\"\n"
  	print >> op_f,"`include \""+proj_rand_test+".sv\"\n"
  	print >> op_f,"  //parameter CLOCK_PERIOD = 10; // Assign clock Period\n"
  	print >> op_f,"  logic clk; \n"
  	print >> op_f,"  "+proj_if_0+" vif(.clk (clk) ); //instantiate uvc interface\n"
  	print >> op_f,"  initial"
  	print >> op_f,"    begin : cgen"
  	print >> op_f,"      clk = 0;"
  	print >> op_f,"      forever #10 clk <= ~clk;"
  	print >> op_f,"    end : cgen\n"
  	print >> op_f,"  //instantiate and connect dut to interface(s) here\n"
  	print >> op_f,"  initial"
  	print >> op_f,"    begin"
  	print >> op_f,"      uvm_config_db#(virtual "+proj_if_0+")::set(.cntxt(null),"
        print >> op_f,"					.inst_name(\"uvm_test_top.env.agent\"),"
        print >> op_f,"					.field_name(\"vif\"),"
        print >> op_f,"					.value(vif));"
	print >> op_f,"      run_test();"
	print >> op_f,"    end\n"
	print >> op_f,"endmodule\n"
        vw_show_progress()
	
def createRunDir() :
	print "Starting Run files..."
	os.mkdir("run_dir")
	createUvmFlist ()
	createMakefile ()
	print ("Run_dir files printed successfully.")
        vw_show_progress()
	
def createSeqTests() :
  	print "Creating sequence test files..."
 	os.mkdir("seq_tests")
	createBaseTest ()
  	createRandSeq ()
  	createRandTest ()
  	createSeqLib ()
  	createTbDutTop ()
        vw_show_progress()
	print "Sequence Tests are created"
        vw_show_progress()

def vw_dvc_uvm () :
	print "Starting VW DVC UVM"
        if os.path.exists(proj_name):
            shutil.rmtree(proj_name, ignore_errors=True)
        
	os.mkdir(proj_name)
	os.chdir(proj_name)
	os.mkdir("dut_src")
	os.mkdir("tb_src")
        vw_show_progress()
	createTransactionheader()
        createTransaction()
	createSequencerheader()
  	createSequencer()      
	createInmonitorheader()
	createInmonitor()
	createOutMonitorheader()
	createOutMonitor()
	createFuncCovheader ()
	createFuncCov ()
	createScoreboardheader()
	createScoreboard()
	createDriverheader()
	createDriver()
	cretaeAgentheader()
	cretaeAgent()
	createEnvheader()
	createEnv()
	createSva()
	createInterface()
	createInclude()
	createPackage ()
  	createSvaBind ()
        createRunDir()
        createSeqTests()
        print 'vw_dvc_uvm: Complete UVM environment for project: ', proj_name, '  created!!'


def vw_show_progress():
  sleep(0.1)
  print(inspect.stack()[1][3])

def vw_run():
    vw_dvc_pid = os.fork()
    if vw_dvc_pid == 0:
      vw_dvc_uvm()
    else:
      createProgressBar()
        
vw_run()

