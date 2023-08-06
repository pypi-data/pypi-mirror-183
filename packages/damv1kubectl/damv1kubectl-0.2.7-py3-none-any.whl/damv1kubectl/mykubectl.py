import damv1env as env
import damv1time7 as time7
import damv1time7.mylogger as Q
import damv1myparamikossh as prmko

import re
from enum import Enum


class strcommandpods(Enum):
    command_for_name_sort_by_ascending = f'''kubectl get pods -n {{ns}} --no-headers'''
    command_for_name_sort_by_descending = f'''kubectl get pods -n {{ns}} --no-headers | sort --key 1 --reverse'''
    command_for_status_sort_by_ascending = f'''kubectl get pods -n {{ns}} --no-headers | sort --key 3'''
    command_for_restart_sort_by_descending = f'''kubectl get pods -n {{ns}} --no-headers | sort --key 4 --numeric --reverse'''
    command_for_age_created_sort_by_ascending = f'''kubectl get pods -n {{ns}} --no-headers --sort-by=.metadata.creationTimestamp'''
    command_for_age_start_sort_by_ascending = f'''kubectl get pods -n {{ns}} --no-headers --sort-by=.status.startTime'''


class sanbox():
    
    def execsshcmd(self, _strcmd):
        oput = None # イニシャライズ
        try:
            if _strcmd.strip():
                srv = env.sandbox_srv # changes this for sandbox / production (  コンフィギュレーション )
                oput = prmko.sshcommand(srv.host._value_, srv.username._value_, srv.port._value_, srv.privatekey._value_, _strcmd, False)
        except Exception as e:
            Q.logger(time7.currentTime7(),'Error Handling ( エラー ):',str(e))
        return oput  


    def getLst_info_allPods_by_ns(self, _ns, OptSortCmd = strcommandpods.command_for_name_sort_by_ascending._value_):
        lst_po = [] # イニシャライズ
        try:
            query = OptSortCmd.format(ns = _ns) # クエリ
            cmd_gtpo = "{0} | awk {{'{1}'}} | column -t".format(query,'print $1"|"$3"|"$4"|"$5$6')
            lst_ipo = self.execsshcmd(cmd_gtpo)
            if len(lst_ipo)!=0:
                fdRow={}
                for row in lst_ipo:
                    sp_ipo = row.split('|')
                    fdRow = {   'name':sp_ipo[0],
                                'status':sp_ipo[1],
                                'restart':sp_ipo[2],
                                'age':sp_ipo[3] }
                    lst_po.append(fdRow)
        except Exception as e:
            Q.logger(time7.currentTime7(),'Error Handling ( エラー ):',str(e))
        return lst_po

    def execCmd_by_regex_strquery(self, _strcmd, target_str=[],**kwargs):
        oput = [] # イニシャライズ
        threadNumber = 0
        idAirtable = None
        DiffMinSecondsSilentLogger_forUpdate = 0
        try:
            if '_argThreadNumber' in kwargs:
                if "'int'" in str(type(threadNumber)):
                    threadNumber = kwargs.get("_argThreadNumber") 
                    if '_argIdAirtable' in kwargs:
                        idAirtable = kwargs.get("_argIdAirtable") 
                        if '_argDiffMinSecondsSilentLogger_forUpdate' in kwargs:
                            DiffMinSecondsSilentLogger_forUpdate = int(kwargs.get("_argDiffMinSecondsSilentLogger_forUpdate"))
            if _strcmd.strip():
                if len(target_str) !=0:
                    for target in target_str:
                        print('\r{0}              Scanning target regex '.format(time7.currentTime7()), end='')

                        Q.logger(time7.currentTime7(),'',_argMarkSilentLogger=True, \
                                    _argDiffMinSecondsSilentLogger_forUpdate = DiffMinSecondsSilentLogger_forUpdate, \
                                    _argThreadNumber=threadNumber, _argIdAirtable=idAirtable)

                        re_target = re.compile(r"({})".format(target), flags=re.IGNORECASE)
                        if re.search(re_target, _strcmd):
                            oput=self.execsshcmd(_strcmd) #  specific objects スペシャルオブジェクト
                else:
                    print('\r{0}              Scanning target regex '.format(time7.currentTime7()), end='')

                    Q.logger(time7.currentTime7(),'',_argMarkSilentLogger=True, \
                                _argDiffMinSecondsSilentLogger_forUpdate = DiffMinSecondsSilentLogger_forUpdate, \
                                _argThreadNumber=threadNumber, _argIdAirtable=idAirtable)

                    oput=self.execsshcmd(_strcmd) # all objects すべてオブジェクト
        except Exception as e:
            Q.logger(time7.currentTime7(),'Error Handling ( エラー ):',str(e))
        return oput 
    
    def getLst_log_pod_by_pattern_andTarget(self, _sincelast, _pod, _namespace, _pattern, _lst_target,**kwargs):
        lst_oput = [] # イニシャライズ
        threadNumber = 0
        idAirtable = None
        DiffMinSecondsSilentLogger_forUpdate = 0
        try:
            if '_argThreadNumber' in kwargs:
                if "'int'" in str(type(threadNumber)):
                    threadNumber = kwargs.get("_argThreadNumber") 
                    if '_argIdAirtable' in kwargs:
                        idAirtable = kwargs.get("_argIdAirtable") 
                        if '_argDiffMinSecondsSilentLogger_forUpdate' in kwargs:
                            DiffMinSecondsSilentLogger_forUpdate = int(kwargs.get("_argDiffMinSecondsSilentLogger_forUpdate"))

            # Notes :
            # sed -r "s/\x1b\[[^@-~]*[@-~]//g"     is for remove ANSI escape sequence
            query = f'kubectl logs --since={_sincelast} --timestamps=true {_pod} -n {_namespace} | sed -r "s/\x1b\[[^@-~]*[@-~]//g" | grep "{_pattern}" | sort -k2 -r | head -n 1'
            lst_oput = self.execCmd_by_regex_strquery(query, _lst_target, _argDiffMinSecondsSilentLogger_forUpdate = DiffMinSecondsSilentLogger_forUpdate, \
                                    _argThreadNumber=threadNumber, _argIdAirtable=idAirtable)
        except Exception as e:
            Q.logger(time7.currentTime7(),'Error Handling ( エラー ):',str(e))
        return lst_oput 










# # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ## uncomments this bellow for testing only ( テスティング ) !
# # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# f = sanbox()
# def excute(_ns):
#     lst_po = []
#     Q.logger(time7.currentTime7(),'Begin ( はじまり )')
#     Q.logger(time7.currentTime7(),'(1) - Loading Process ( ローディング )')
#     lst_po = f.getLst_info_allPods_by_ns('sit')
#     print(lst_po)

# excute('sit')