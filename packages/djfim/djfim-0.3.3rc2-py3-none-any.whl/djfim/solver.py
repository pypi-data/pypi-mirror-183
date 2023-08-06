# -*- python -*-
#
# Copyright 2021, 2022 Cecelia Chen
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# djfim.solver

from django.apps import apps
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.topological_sort import stable_topological_sort


class DMSolver(object):

    def get_model_class(self, app_label, model_name):
        '''
        :param app_label: (string)
        :param model_name: (string)
        '''
        mod = apps.get_app_config(app_label).get_model(model_name)
        return mod


class SortSolver(object):
    def get_stable_sort(self, workset):
        g = dict()
        for each in workset:
            dm = self.dm_solver.get_dm(each)
            dependency = DependencySolver(dm).get_dependency()
            g[ dm ] = dependency
        return stable_topological_sort(g.keys(), g)


class DependencySolver(object):

    def __init__(self, dm):
        super().__init__()
        self.dm = dm
        #
        self.load_preset()

    def load_preset(self):
        self.d_types = (
            models.ForeignKey,
            models.OneToOneField
        )

        self.user_dm = get_user_model()
        self.masked_t = (
            self.dm._meta.label,
            self.user_dm._meta.label,
        )
        return self

    def accept(self, f):
        rval = isinstance(f, self.d_types)
        return rval

    def reject(self, f):
        # skip self-referencing link or known target set;
        rval = ( f._meta.label in self.masked_t )
        return rval

    def get_dependency(self):
        t = set()
        field_list = self.dm._meta.fields
        for f in field_list:
            if self.accept(f):
                if self.reject(f):
                    continue
                t.add(f)
        return t


class LinkSolver(object):
    '''
    solve the immediate dependency
    '''

    def find_local_mapped_entry(self):
        MODEL = self.getMappedModel()
        linked_rec = None
        try:
            if self.local_pk is None:
                raise ValueError('no local mapping saved')
            linked_rec = MODEL.objects.get(id=self.local_pk)
        except (MODEL.DoesNotExist, MODEL.MultipleObjectsReturned) as e:
            # NOTE: may need to handle the NotFound exception explicitly
            raise RecordException(e, self)
            pass
        return linked_rec

    def create_local_record(self, context, **kwargs):
        '''
        NOTE: this method may throw exception if DB constraint is violated.

        :param context: this dictionary will be updated within this method (dict)

        :return: `Model` instance
        '''
        MODEL = self.getMappedModel()
        fk_lst = self.getFKList(MODEL)
        local_remap = self.extract_fk_map(fk_lst, context, **kwargs)
        record = MODEL(
            **(
                self.patch_upstream_data(
                    self.data,
                    local_map=local_remap
                )
            )
        )
        #try:
        record.save()
        # post_save: a) update working context;
        new_rec_key = self.getTargetContextKey(MODEL, self.upstream_pk)
        context[new_rec_key] = record.id
        #except MODEL.ConstraintError as e:
        #    raise RecordException(e, self)
        # post_save: b) save the map;
        self.local_pk = record.id
        self.save(update_fields=['local_pk',])
        return record


class MergeSolver(object):
    '''
    solve data conflict during merge.
    '''

    def compareRecord(self, local_rec, upstream_rec, **kwargs):
        '''
        :param local_rec: (`Model` instance)
        :param upstream_rec: ()
        TODO: not fully implemented yet
        compareRecord(self.find_local_mapped_entry(), self.getMappedModel()(**self.data))
        '''
        cmp_ret = dict()

        MODEL = self.getMappedModel()
        field_lst = MODEL._meta.fields

        for field in field_lst:
            field_name = field.attname
            if isinstance(field, models.ForeignKey):
                try:
                    fk_cmp = self.checkFKMap(field, local_rec, upstream_rec)
                    if fk_cmp is None:
                        cmp_ret[field_name] = True
                    else:
                        cmp_ret[field_name] = fk_cmp
                except ValueError:
                    cmp_ret[field_name] = False
                    # NOTE: may need to deal with the missing record, or log this exception
                    #raise
            else:
                cmp_ret[field_name] = getattr(loca_rec, field_name) == getattr(upstream_rec, field_name)
        return cmp_ret
